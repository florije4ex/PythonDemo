package com.szy.searchcenter.service.impl;


import com.szy.searchcenter.model.StatSchoolRecordInfo;
import com.szy.searchcenter.openservice.model.StatSchoolRecordInfoDto;
import com.szy.searchcenter.utils.LocalCacheUtils;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.alibaba.fastjson.JSON;
import com.szy.core.config.SearchCenterConfig;
import com.szy.searchcenter.contants.SearchCenterContants;
import com.szy.searchcenter.dao.ISearchDao;
import com.szy.searchcenter.model.CacheObject;
import com.szy.searchcenter.model.StatUserDetailInfo;
import com.szy.searchcenter.openservice.facade.ISearchFacade;
import com.szy.searchcenter.openservice.model.StatUserDetailInfoDto;
import com.szy.searchcenter.share.DbQpsLimitCounter;
import com.szy.searchcenter.utils.BeanUtils;

@Service("searchFacade")
public class SearchServiceImpl implements ISearchFacade {

    @Autowired
    ISearchDao searchDao;

    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @Override
    public StatUserDetailInfoDto getStatUserInfo(String userId) {
        StatUserDetailInfoDto userRecordInfoDto = new StatUserDetailInfoDto();
        //看缓存里有没有
        CacheObject cacheObject = LocalCacheUtils.getValueFromLocalCache(SearchCenterContants.STAT_USER_RECORD_INFO, userId, CacheObject.class);
        //看缓存里有没有过期
        if (cacheObject != null) {
            return JSON.parseObject(cacheObject.getModel(), StatUserDetailInfoDto.class);
        }
        //限流操作,如果访问数据库的频次超过xx次，就直接取缓存里的数据
        int count = DbQpsLimitCounter.count.incrementAndGet();
        if (count >= SearchCenterConfig.getDbQpsLimit().intValue()) {
            logger.info("被限速了，当前频次为" + count + ",取旧的缓存数据:" + cacheObject.getModel());
            return JSON.parseObject(cacheObject.getModel(), StatUserDetailInfoDto.class);
        }

        //数据库里load出来
        StatUserDetailInfo userInfo = searchDao.getStatUserInfo(userId);
        if (userInfo == null) {
            return null;
        }

        BeanUtils.copyProperties(userInfo, userRecordInfoDto);

        //设置回缓存里
        cacheObject.setTime(System.currentTimeMillis());
        cacheObject.setModel(JSON.toJSONString(userRecordInfoDto));
        LocalCacheUtils.putValue2LocalCache(SearchCenterContants.STAT_USER_RECORD_INFO, userId, cacheObject, SearchCenterConfig.getCacheTimeOut());
        return userRecordInfoDto;
    }

    @Override
    public StatSchoolRecordInfoDto getStatSchoolInfo(String schoolId) {
        StatSchoolRecordInfoDto schoolRecordInfoDto = new StatSchoolRecordInfoDto();
        CacheObject cacheObject = LocalCacheUtils.getValueFromLocalCache(SearchCenterContants.STAT_SCHOOL_RECORD_INFO, schoolId, CacheObject.class);
        //看缓存里有没有过期
        if (cacheObject != null) {
            return JSON.parseObject(cacheObject.getModel(), StatSchoolRecordInfoDto.class);
        }

        //限流操作,如果访问数据库的频次超过xx次，就直接取缓存里的数据
        int count = DbQpsLimitCounter.count.incrementAndGet();
        if (count >= SearchCenterConfig.getDbQpsLimit().intValue()) {
            logger.info("被限速了，当前频次为" + count + ",取旧的缓存数据:" + cacheObject.getModel());
            return JSON.parseObject(cacheObject.getModel(), StatSchoolRecordInfoDto.class);
        }

        //数据库里load出来
        StatSchoolRecordInfo schoolInfo = searchDao.getStatSchoolInfo(schoolId);
        if (schoolInfo == null) {
            return null;
        }

        BeanUtils.copyProperties(schoolInfo, schoolRecordInfoDto);

        //设置回缓存里
        cacheObject.setTime(System.currentTimeMillis());
        cacheObject.setModel(JSON.toJSONString(schoolRecordInfoDto));
        LocalCacheUtils.putValue2LocalCache(SearchCenterContants.STAT_SCHOOL_RECORD_INFO, schoolId, cacheObject, SearchCenterConfig.getCacheTimeOut());

        return schoolRecordInfoDto;
    }
}
