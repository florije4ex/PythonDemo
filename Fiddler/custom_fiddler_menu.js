//https://www.cnblogs.com/zhm450/p/6770595.html
//https://www.cnblogs.com/zhm450/p/6434664.html  Fiddler插件 --- 解密Elong Mapi请求参数及响应内容
//https://github.com/jessemcdowell/FiddlerMessagePackViewer
//https://github.com/waf/WCF-Binary-Message-Inspector
//https://segmentfault.com/a/1190000021840906
//映射线上Host到灰度等测试环境； 在class中增加如下代码
RulesString("HostMapping",true)
RulesStringValue(0,"灰度1", "10.35.45.84")
RulesStringValue(1,"灰度2", "10.35.45.84:8080")
RulesStringValue(2,"233.94", "192.168.233.94")
RulesStringValue(3,"14.206", "192.168.14.206")
RulesStringValue(4,"9.28", "192.168.9.28")
public static var m_host: String = null;

// 在 OnBeforeRequest 方法中增加如下

if(null != m_host && oSession.HostnameIs("mobile-api2011.elong.com") ){

	oSession.host=m_host;

}

//替换DeviceID，模拟MVT测试及新用户
//在class中增加如下代码

RulesString("ABTest测试",true)
RulesStringValue(0,"测试组", "12345678-1234-5678-9012-123456789010")
RulesStringValue(1,"对照组", "12345678-1234-5678-9012-123456789011")
RulesStringValue(2,"新用户", "12345678-1234-5678-9012-122211133344")
public static var m_deviceid: String = null;

// 在 OnBeforeRequest 方法中增加如下
if(null != m_deviceid && oSession.oRequest.headers.Exists("DeviceId") &&oSession.oRequest.headers.Exists("ClientType") ){
    oSession.oRequest["DeviceId"] = m_deviceid;
}

//通过设置网络延时，来模拟不同的网速场景
//在class中增加如下代码 ；增加菜单项
RulesString("网速模拟",true)
RulesStringValue(0,"Simulate &Modem Speeds", "150")
RulesStringValue(1,"Simulate 2G(25KB)", "40")
RulesStringValue(2,"Simulate 3G(250KB)", "4")
public static var m_networkSpeed: String = null;

// 在 OnBeforeRequest 方法中增加如下
if(m_networkSpeed){
    //网速模拟测试
    oSession["request-trickle-delay"] = (parseInt(m_networkSpeed)*2).ToString();
    oSession["response-trickle-delay"] = m_networkSpeed;
}

//在class中增加如下代码
//增加菜单项
public static RulesOption("标记HTTPS", "Other")
var m_https: boolean = false;

//只展示来自APP的Mapi请求，其它类型全部过滤
public static RulesOption("Only Show Mapi", "Other")
var m_OnlyMapi: boolean = false;


// 在 OnBeforeRequest 方法中增加如下

//将域名中包含elong的HTTPS请求，标记为红色
if ( m_https && oSession.isHTTPS && oSession.fullUrl.indexOf("elong")>0){
	oSession["ui-color"] = "red";
}

//只展示APP过来的请求，非app请求直接过滤掉
if(m_OnlyMapi && !oSession.oRequest.headers.Exists("DeviceId") && !oSession.oRequest.headers.Exists("ClientType")){
	oSession["ui-hide"] = "true";
}

//在class中增加如下代码即可

public static BindUIColumn("ClientIP", 120)
function FillClientIPColumn(oS: Session): String {
    //oS.oResponse.headers.
	return oS.clientIP.Split(':')[3];
}

public static BindUIColumn("Method", 60)
function FillMethodColumn(oS: Session): String {
    return oS.RequestMethod;
}