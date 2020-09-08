static function OnBeforeResponse(oSession: Session) {
        if (m_Hide304s && oSession.responseCode == 304) {
            oSession["ui-hide"] = "true";
        }
        if ( m_showMarkString && oSession.uriContains("szy.com")) {
            //以decode格式解码  parent/dynamic/config/v1.0
            oSession.utilDecodeResponse();
            //需要标记的字符串
            var oFindStrings = new Array('strategy');

            // For each target string, check the response to see if it's present.
            var iEach = 0;

            oSession["ui-customcolumn"] = String.Empty;

            for (iEach; iEach < oFindStrings.length; iEach++) {
                if (oSession.utilFindInResponse(oFindStrings[iEach], false) > 0) {
                    //标记颜色
                    oSession["ui-color"] = "#EE00EE";
                    //加粗
                    oSession["ui-bold"] = "true";
                    //在custom标识response中有的关键字
                    oSession["ui-customcolumn"] += oFindStrings[iEach] + "; ";
                }
            }
        }



        if (m_showReplaceString && oSession.uriContains("szy")) {
            //以decode格式解码
            oSession.utilDecodeResponse();

            //oSession["ui-color"] = "#B03060";
			//替换前字符串
			var oReplaceStrings = new Array('"body":{"popwindow":[]}'); //{"showtime":0,"popcode":"1117"}
			//替换后字符串
			var oNewStings= new Array('"body":{"popwindow":[{"showtime":0,"popcode":"1103"}]}')

            //oSession.oRequest.headers.Add("X-Forwarded-For", "203.161.32.141");   // 添加一个参数，新加坡ip
            var iEach=0;


            oSession["ui-customcolumn"]=String.Empty;

            for (iEach; iEach<oReplaceStrings.length; iEach++){
                // if true
                if (oSession.utilReplaceInResponse(oReplaceStrings[iEach], oNewStings[iEach])){
                    //标记颜色
                    oSession["ui-color"]="#B03060";
                    //加粗
                    oSession["ui-bold"]="true";
                    //在custom标识response中被替换的字符串
                    oSession["ui-customcolumn"] += oReplaceStrings[iEach]+";  ";
                }

            }

        }

        if (m_showReplaceString && oSession.uriContains("szy")) {
            //以decode格式解码
            oSession.utilDecodeResponse();

            //oSession["ui-color"] = "#B03060";
			//替换前字符串
			var oldStrings = new Array('"body":{"popwindow":[]}');
			//替换后字符串
			var oNewStings= new Array('"body":{"popwindow":[{"showtime":0,"popcode":"1103"}]}')

            //oSession.oRequest.headers.Add("X-Forwarded-For", "203.161.32.141");   // 添加一个参数，新加坡ip
            var iEach=0;


            oSession["ui-customcolumn"]=String.Empty;

            for (iEach; iEach<oReplaceStrings.length; iEach++){
                // if true
                if (oSession.utilReplaceInResponse(oldStrings[iEach], oNewStings[iEach])){
                    //标记颜色
                    oSession["ui-color"]="#B04060";
                    //加粗
                    oSession["ui-bold"]="true";
                    //在custom标识被替换的字符串
                    oSession["ui-customcolumn"] += oldStrings[iEach]+";  ";
                }

            }

        }

        //直接替换request body中的数据
        if (m_showReplaceString && oSession.uriContains("szy")) {
            //以decode格式解码
            //oSession.utilDecodeResponse();
            oSession.GetRequestBodyAsString()

            //oSession["ui-color"] = "#B03060";
			//替换前字符串
			var oldStrings = new Array('"studentId":"1e83bba94139a4d152e9"');
			//替换后字符串
			var oNewStings= new Array('"studentId":"1e83bba94139a4d15233"')

            //oSession.oRequest.headers.Add("X-Forwarded-For", "203.161.32.141");   // 添加一个参数，新加坡ip
            var iEach=0;


            oSession["ui-customcolumn"]=String.Empty;

            for (iEach; iEach<oldStrings.length; iEach++){
                // if true
                if (oSession.utilReplaceInRequest(oldStrings[iEach], oNewStings[iEach])){
                    //标记颜色
                    oSession["ui-color"]="#B04060";
                    //加粗
                    oSession["ui-bold"]="true";
                    //在custom标识被替换的字符串
                    oSession["ui-customcolumn"] += oldStrings[iEach]+";  ";
                }

            }

        }

        //直接替换request body中的数据
		if (m_showRequestReplaceString && oSession.uriContains("szy")) {
			//以decode格式解码
			//oSession.utilDecodeResponse();
			oSession.GetRequestBodyAsString()

			//oSession["ui-color"] = "#B03060";
			//替换前字符串
			var oldStrings = new Array('"studentId":"1e83bba94139a4d152e9"');
			//替换后字符串
			var oNewStings= new Array('"studentId":"1e83bba94139a4d15233"')

			//oSession.oRequest.headers.Add("X-Forwarded-For", "203.161.32.141");   // 添加一个参数，新加坡ip
			var iEach=0;


			oSession["ui-customcolumn"]=String.Empty;

			for (iEach; iEach<oldStrings.length; iEach++){
				// if true
				if (oSession.utilReplaceInRequest(oldStrings[iEach], oNewStings[iEach])){
					//标记颜色
					oSession["ui-color"]="#B04060";
					//加粗
					oSession["ui-bold"]="true";
					//在custom标识被替换的字符串
					oSession["ui-customcolumn"] += oldStrings[iEach]+";  ";
				}

			}

		}


        //oSession.oRequest["X-Forwarded-For"]="59.125.205.87";


public static RulesOption("标记返回值指定string")
    var m_showMarkString: boolean = false;

    public static RulesOption("替换返回值指定string")
    var m_showReplaceString: boolean = false;

    static function OnBeforeResponse(oSession: Session) {
        if (m_Hide304s && oSession.responseCode == 304) {
            oSession["ui-hide"] = "true";
        }
        if ( m_showMarkString && oSession.uriContains("szy.com")){
            //以decode格式解码  parent/dynamic/config/v1.0
            oSession.utilDecodeResponse();
            //需要标记的字符串
            var oFindStrings = new Array('"studentId":"65029f8c4b4405a835f3"');
			//替换后字符串
			var oNewStings= new Array('"studentId":"65029f8c4b4405a835f3"')

            // For each target string, check the response to see if it's present.
            var iEach=0;

            oSession["ui-customcolumn"]=String.Empty;

            for (iEach; iEach<oFindStrings.length; iEach++){
                if (oSession.utilReplaceInResponse(oFindStrings[iEach], oNewStings[iEach] )) {
                    //标记颜色
                    oSession["ui-color"]="#EE00EE";
                    //加粗
                    oSession["ui-bold"]="true";
                    //在custom标识re中有的关键字
                    oSession["ui-customcolumn"] += oFindStrings[iEach]+"; ";
                }
            }


        }
        if (m_showReplaceString && oSession.uriContains("szy")) {
            //以decode格式解码
            oSession.utilDecodeResponse();

            //oSession["ui-color"] = "#B03060";
			//替换前字符串
			var oReplaceStrings = new Array('"body":{"popwindow":[]}'); //{"showtime":0,"popcode":"1117"}
			//替换后字符串
			var oNewStings= new Array('"body":{"popwindow":[{"showtime":0,"popcode":"1103"}]}')

            //oSession.oRequest.headers.Add("X-Forwarded-For", "203.161.32.141");   // 添加一个参数，新加坡ip
            var iEach=0;


            oSession["ui-customcolumn"]=String.Empty;

            for (iEach; iEach<oReplaceStrings.length; iEach++){
                // if true
                if (oSession.utilReplaceInResponse(oReplaceStrings[iEach], oNewStings[iEach])){
                    //标记颜色
                    oSession["ui-color"]="#B03060";
                    //加粗
                    oSession["ui-bold"]="true";
                    //在custom标识response中被替换的字符串
                    oSession["ui-customcolumn"] += oReplaceStrings[iEach]+";  ";
                }

            }

        }
    }