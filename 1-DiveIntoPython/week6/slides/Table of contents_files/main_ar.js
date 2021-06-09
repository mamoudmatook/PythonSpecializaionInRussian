(function(){/*

 Copyright The Closure Library Authors.
 SPDX-License-Identifier: Apache-2.0
*/
var a=this||self;function d(b,m){b=b.split(".");var c=a;b[0]in c||"undefined"==typeof c.execScript||c.execScript("var "+b[0]);for(var e;b.length&&(e=b.shift());)b.length||void 0===m?c[e]&&c[e]!==Object.prototype[e]?c=c[e]:c=c[e]={}:c[e]=m}function f(b){return b};var g={},MSG_TRANSLATE="\u062a\u0631\u062c\u0645\u0629";g[0]=MSG_TRANSLATE;var MSG_CANCEL="\u0625\u0644\u063a\u0627\u0621";g[1]=MSG_CANCEL;var MSG_CLOSE="\u0625\u063a\u0644\u0627\u0642";g[2]=MSG_CLOSE;function MSGFUNC_PAGE_TRANSLATED_TO(b){return"\u062a\u0631\u062c\u0645 \u0645\u062d\u0631\u0643 \u0627\u0644\u0628\u062d\u062b Google \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629 \u062a\u0644\u0642\u0627\u0626\u064a\u064b\u0627 \u0625\u0644\u0649: "+b}g[3]=MSGFUNC_PAGE_TRANSLATED_TO;
function MSGFUNC_TRANSLATED_TO(b){return"\u062a\u0645\u062a \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0625\u0644\u0649: "+b}g[4]=MSGFUNC_TRANSLATED_TO;var MSG_GENERAL_ERROR="\u062e\u0637\u0623: \u062a\u0639\u0630\u0631 \u0625\u0643\u0645\u0627\u0644 \u0627\u0644\u062e\u0627\u062f\u0645 \u0644\u0637\u0644\u0628\u0643. \u0623\u0639\u062f \u0627\u0644\u0645\u062d\u0627\u0648\u0644\u0629 \u0644\u0627\u062d\u0642\u064b\u0627.";g[5]=MSG_GENERAL_ERROR;var MSG_LEARN_MORE="\u0645\u0632\u064a\u062f \u0645\u0646 \u0627\u0644\u0645\u0639\u0644\u0648\u0645\u0627\u062a";
g[6]=MSG_LEARN_MORE;function MSGFUNC_POWERED_BY(b){return"\u062a\u062f\u0639\u0645\u0647 "+b}g[7]=MSGFUNC_POWERED_BY;var MSG_TRANSLATE_PRODUCT_NAME="\u062a\u0631\u062c\u0645\u0629";g[8]=MSG_TRANSLATE_PRODUCT_NAME;var MSG_TRANSLATION_IN_PROGRESS="\u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0642\u064a\u062f \u0627\u0644\u062a\u0642\u062f\u0645";g[9]=MSG_TRANSLATION_IN_PROGRESS;
function MSGFUNC_TRANSLATE_PAGE_TO(b){return"\u0647\u0644 \u062a\u0631\u064a\u062f \u062a\u0631\u062c\u0645\u0629 \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629 \u0625\u0644\u0649: "+(b+" \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u062e\u062f\u0645\u0629 \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0645\u0646 Google\u061f")}g[10]=MSGFUNC_TRANSLATE_PAGE_TO;
function MSGFUNC_VIEW_PAGE_IN(b){return"\u0639\u0631\u0636 \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629 \u0628\u0627\u0644\u0644\u063a\u0629: "+b}g[11]=MSGFUNC_VIEW_PAGE_IN;var MSG_RESTORE="\u0625\u0638\u0647\u0627\u0631 \u0627\u0644\u0623\u0635\u0644";g[12]=MSG_RESTORE;var MSG_SSL_INFO_LOCAL_FILE="\u0633\u064a\u062a\u0645 \u0625\u0631\u0633\u0627\u0644 \u0645\u062d\u062a\u0648\u0649 \u0647\u0630\u0627 \u0627\u0644\u0645\u0644\u0641 \u0627\u0644\u0645\u062d\u0644\u064a \u0625\u0644\u0649 Google \u0644\u062a\u0631\u062c\u0645\u062a\u0647 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0627\u062a\u0635\u0627\u0644 \u0622\u0645\u0646.";
g[13]=MSG_SSL_INFO_LOCAL_FILE;var MSG_SSL_INFO_SECURE_PAGE="\u0633\u064a\u062a\u0645 \u0625\u0631\u0633\u0627\u0644 \u0645\u062d\u062a\u0648\u0649 \u0647\u0630\u0647 \u0627\u0644\u0635\u0641\u062d\u0629 \u0627\u0644\u0622\u0645\u0646\u0629 \u0625\u0644\u0649 Google \u0644\u062a\u0631\u062c\u0645\u062a\u0647 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0627\u062a\u0635\u0627\u0644 \u0622\u0645\u0646.";g[14]=MSG_SSL_INFO_SECURE_PAGE;var MSG_SSL_INFO_INTRANET_PAGE="\u0633\u064a\u062a\u0645 \u0625\u0631\u0633\u0627\u0644 \u0645\u062d\u062a\u0648\u0649 \u0635\u0641\u062d\u0629 \u0627\u0644\u0634\u0628\u0643\u0629 \u0627\u0644\u062f\u0627\u062e\u0644\u064a\u0629 \u0647\u0630\u0647 \u0625\u0644\u0649 Google \u0644\u062a\u0631\u062c\u0645\u062a\u0647 \u0628\u0627\u0633\u062a\u062e\u062f\u0627\u0645 \u0627\u062a\u0635\u0627\u0644 \u0622\u0645\u0646.";
g[15]=MSG_SSL_INFO_INTRANET_PAGE;var MSG_SELECT_LANGUAGE="\u0627\u062e\u062a\u064a\u0627\u0631 \u0627\u0644\u0644\u063a\u0629";g[16]=MSG_SELECT_LANGUAGE;function MSGFUNC_TURN_OFF_TRANSLATION(b){return"\u0625\u064a\u0642\u0627\u0641 \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0645\u0646 "+b}g[17]=MSGFUNC_TURN_OFF_TRANSLATION;function MSGFUNC_TURN_OFF_FOR(b){return"\u0625\u064a\u0642\u0627\u0641 \u0644\u0644\u063a\u0629: "+b}g[18]=MSGFUNC_TURN_OFF_FOR;var MSG_ALWAYS_HIDE_AUTO_POPUP_BANNER="\u0625\u062e\u0641\u0627\u0621 \u062f\u0627\u0626\u0645\u064b\u0627";
g[19]=MSG_ALWAYS_HIDE_AUTO_POPUP_BANNER;var MSG_ORIGINAL_TEXT="\u0627\u0644\u0646\u0635 \u0627\u0644\u0623\u0635\u0644\u064a:";g[20]=MSG_ORIGINAL_TEXT;var MSG_FILL_SUGGESTION="\u0627\u0644\u0645\u0633\u0627\u0647\u0645\u0629 \u0628\u062a\u0631\u062c\u0645\u0629 \u0623\u0641\u0636\u0644";g[21]=MSG_FILL_SUGGESTION;var MSG_SUBMIT_SUGGESTION="\u0645\u0633\u0627\u0647\u0645\u0629";g[22]=MSG_SUBMIT_SUGGESTION;var MSG_SHOW_TRANSLATE_ALL="\u062a\u0631\u062c\u0645\u0629 \u0627\u0644\u0643\u0644";g[23]=MSG_SHOW_TRANSLATE_ALL;
var MSG_SHOW_RESTORE_ALL="\u0627\u0633\u062a\u0631\u062f\u0627\u062f \u0627\u0644\u0643\u0644";g[24]=MSG_SHOW_RESTORE_ALL;var MSG_SHOW_CANCEL_ALL="\u0625\u0644\u063a\u0627\u0621 \u0627\u0644\u0643\u0644";g[25]=MSG_SHOW_CANCEL_ALL;var MSG_TRANSLATE_TO_MY_LANGUAGE="\u062a\u0631\u062c\u0645\u0629 \u0627\u0644\u0623\u0642\u0633\u0627\u0645 \u0625\u0644\u0649 \u0644\u063a\u062a\u064a";g[26]=MSG_TRANSLATE_TO_MY_LANGUAGE;
function MSGFUNC_TRANSLATE_EVERYTHING_TO(b){return"\u062a\u0631\u062c\u0645\u0629 \u0643\u0644 \u0634\u064a\u0621 \u0625\u0644\u0649 "+b}g[27]=MSGFUNC_TRANSLATE_EVERYTHING_TO;var MSG_SHOW_ORIGINAL_LANGUAGES="\u0625\u0638\u0647\u0627\u0631 \u0627\u0644\u0644\u063a\u0627\u062a \u0627\u0644\u0623\u0635\u0644\u064a\u0629";g[28]=MSG_SHOW_ORIGINAL_LANGUAGES;var MSG_OPTIONS="\u062e\u064a\u0627\u0631\u0627\u062a";g[29]=MSG_OPTIONS;var MSG_TURN_OFF_TRANSLATION_FOR_THIS_SITE="\u0625\u064a\u0642\u0627\u0641 \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0644\u0647\u0630\u0627 \u0627\u0644\u0645\u0648\u0642\u0639";
g[30]=MSG_TURN_OFF_TRANSLATION_FOR_THIS_SITE;g[31]=null;var MSG_ALT_SUGGESTION="\u0639\u0631\u0636 \u0627\u0644\u062a\u0631\u062c\u0645\u0627\u062a \u0627\u0644\u0628\u062f\u064a\u0644\u0629";g[32]=MSG_ALT_SUGGESTION;var MSG_ALT_ACTIVITY_HELPER_TEXT="\u0627\u0646\u0642\u0631 \u0639\u0644\u0649 \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0623\u0639\u0644\u0627\u0647 \u0644\u0639\u0631\u0636 \u0627\u0644\u062a\u0631\u062c\u0645\u0627\u062a \u0627\u0644\u0628\u062f\u064a\u0644\u0629.";g[33]=MSG_ALT_ACTIVITY_HELPER_TEXT;
var MSG_USE_ALTERNATIVES="\u0627\u0633\u062a\u062e\u062f\u0627\u0645";g[34]=MSG_USE_ALTERNATIVES;var MSG_DRAG_TIP="\u0627\u0633\u062d\u0628 \u0645\u0639 \u0627\u0644\u0636\u063a\u0637 \u0639\u0644\u0649 \u0627\u0644\u0645\u0641\u062a\u0627\u062d shift \u0644\u0625\u0639\u0627\u062f\u0629 \u0627\u0644\u062a\u0631\u062a\u064a\u0628.";g[35]=MSG_DRAG_TIP;var MSG_CLICK_FOR_ALT="\u0627\u0646\u0642\u0631 \u0644\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u062a\u0631\u062c\u0645\u0627\u062a \u0628\u062f\u064a\u0644\u0629";
g[36]=MSG_CLICK_FOR_ALT;var MSG_DRAG_INSTUCTIONS="\u0627\u0636\u063a\u0637 \u0645\u0639 \u0627\u0644\u0627\u0633\u062a\u0645\u0631\u0627\u0631 \u0639\u0644\u0649 \u0627\u0644\u0645\u0641\u062a\u0627\u062d shift\u060c \u062b\u0645 \u0627\u0646\u0642\u0631 \u0645\u0639 \u0633\u062d\u0628 \u0627\u0644\u0643\u0644\u0645\u0627\u062a \u0623\u0639\u0644\u0627\u0647 \u0644\u0625\u0639\u0627\u062f\u0629 \u062a\u0631\u062a\u064a\u0628\u0647\u0627.";g[37]=MSG_DRAG_INSTUCTIONS;var MSG_SUGGESTION_SUBMITTED="\u0634\u0643\u0631\u0627\u064b \u0644\u0645\u0633\u0627\u0647\u0645\u062a\u0643 \u0641\u064a \u062a\u0642\u062f\u064a\u0645 \u0627\u0642\u062a\u0631\u0627\u062d \u062d\u0648\u0644 \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0641\u064a \u062e\u062f\u0645\u0629 Google \u0644\u0644\u062a\u0631\u062c\u0645\u0629.";
g[38]=MSG_SUGGESTION_SUBMITTED;var MSG_MANAGE_TRANSLATION_FOR_THIS_SITE="\u0625\u062f\u0627\u0631\u0629  \u0627\u0644\u062a\u0631\u062c\u0645\u0629 \u0644\u0644\u0645\u0648\u0642\u0639 \u0627\u0644\u0625\u0644\u0643\u062a\u0631\u0648\u0646\u064a \u0647\u0630\u0627";g[39]=MSG_MANAGE_TRANSLATION_FOR_THIS_SITE;var MSG_ALT_AND_CONTRIBUTE_ACTIVITY_HELPER_TEXT="\u064a\u0645\u0643\u0646\u0643 \u0627\u0644\u0646\u0642\u0631 \u0639\u0644\u0649 \u0643\u0644\u0645\u0629 \u0644\u0644\u062d\u0635\u0648\u0644 \u0639\u0644\u0649 \u062a\u0631\u062c\u0645\u0627\u062a \u0628\u062f\u064a\u0644\u0629\u060c \u0623\u0648 \u0627\u0644\u0646\u0642\u0631 \u0645\u0631\u0651\u062a\u064a\u0646 \u0644\u0644\u062a\u0639\u062f\u064a\u0644 \u0645\u0628\u0627\u0634\u0631\u0629";
g[40]=MSG_ALT_AND_CONTRIBUTE_ACTIVITY_HELPER_TEXT;var MSG_ORIGINAL_TEXT_NO_COLON="\u0627\u0644\u0646\u0635 \u0627\u0644\u0623\u0635\u0644\u064a";g[41]=MSG_ORIGINAL_TEXT_NO_COLON;g[42]="\u062a\u0631\u062c\u0645\u0629";g[43]="\u062a\u0631\u062c\u0645\u0629";g[44]="\u062a\u0645 \u0625\u0631\u0633\u0627\u0644 \u0627\u0644\u062a\u0635\u062d\u064a\u062d.";var MSG_LANGUAGE_UNSUPPORTED="\u062e\u0637\u0623: \u0644\u063a\u0629 \u0635\u0641\u062d\u0629 \u0648\u064a\u0628 \u063a\u064a\u0631 \u0645\u0639\u062a\u0645\u062f\u0629.";
g[45]=MSG_LANGUAGE_UNSUPPORTED;var MSG_LANGUAGE_TRANSLATE_WIDGET="\u0623\u062f\u0627\u0629 \u062a\u0631\u062c\u0645\u0629 \u0627\u0644\u0644\u063a\u0629";g[46]=MSG_LANGUAGE_TRANSLATE_WIDGET;var h;function k(b,m){this.g=m===l?b:""}k.prototype.toString=function(){return this.g+""};var l={};var n=window.google&&google.translate&&google.translate._const;
if(n){var p;a:{for(var q=[],r=[""],t=0;t<r.length;++t){var u=r[t].split(","),v=u[0];if(v){var w=Number(u[1]);if(!(!w||.1<w||0>w)){var x=Number(u[2]),y=new Date,z=1E4*y.getFullYear()+100*(y.getMonth()+1)+y.getDate();!x||x<z||q.push({version:v,ratio:w,h:x})}}}var A=0,B=window.location.href.match(/google\.translate\.element\.random=([\d\.]+)/),C=Number(B&&B[1])||Math.random();for(t=0;t<q.length;++t){var D=q[t];A+=D.ratio;if(1<=A)break;if(C<A){p=D.version;break a}}p="TE_20210503_00"}var E="/element/%s/e/js/element/element_main.js".replace("%s",
p);if("0"==p){var F=" element %s e js element element_main.js".split(" ");F[F.length-1]="main_ar.js";E=F.join("/").replace("%s",p)}if(n._cjlc)n._cjlc(n._pas+n._pah+E);else{var G=n._pas+n._pah+E,H,I="SCRIPT",J=document;I=String(I);"application/xhtml+xml"===J.contentType&&(I=I.toLowerCase());H=J.createElement(I);H.type="text/javascript";H.charset="UTF-8";var K,L;if(void 0===h){var M=null,N=a.trustedTypes;if(N&&N.createPolicy){try{M=N.createPolicy("goog#html",{createHTML:f,createScript:f,createScriptURL:f})}catch(b){a.console&&
a.console.error(b.message)}h=M}else h=M}var O=(L=h)?L.createScriptURL(G):G;K=new k(O,l);H.src=K instanceof k&&K.constructor===k?K.g:"type_error:TrustedResourceUrl";var P,Q,R=(H.ownerDocument&&H.ownerDocument.defaultView||window).document,S=null===(Q=R.querySelector)||void 0===Q?void 0:Q.call(R,"script[nonce]");(P=S?S.nonce||S.getAttribute("nonce")||"":"")&&H.setAttribute("nonce",P);var T=document.getElementsByTagName("head")[0];T||(T=document.body.parentNode.appendChild(document.createElement("head")));
T.appendChild(H)}d("google.translate.m",g);d("google.translate.v",p)};}).call(window)
