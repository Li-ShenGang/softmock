(this["webpackJsonpsoft-mock-template"]=this["webpackJsonpsoft-mock-template"]||[]).push([[107],{1616:function(e,t,n){!function(e){"use strict";e.defineMode("tiki",(function(e){function t(e,t,n){return function(i,o){for(;!i.eol();){if(i.match(t)){o.tokenize=r;break}i.next()}return n&&(o.tokenize=n),e}}function n(e){return function(t,n){for(;!t.eol();)t.next();return n.tokenize=r,e}}function r(e,i){function o(t){return i.tokenize=t,t(e,i)}var a=e.sol(),u=e.next();switch(u){case"{":return e.eat("/"),e.eatSpace(),e.eatWhile(/[^\s\u00a0=\"\'\/?(}]/),i.tokenize=f,"tag";case"_":if(e.eat("_"))return o(t("strong","__",r));break;case"'":if(e.eat("'"))return o(t("em","''",r));break;case"(":if(e.eat("("))return o(t("variable-2","))",r));break;case"[":return o(t("variable-3","]",r));case"|":if(e.eat("|"))return o(t("comment","||"));break;case"-":if(e.eat("="))return o(t("header string","=-",r));if(e.eat("-"))return o(t("error tw-deleted","--",r));break;case"=":if(e.match("=="))return o(t("tw-underline","===",r));break;case":":if(e.eat(":"))return o(t("comment","::"));break;case"^":return o(t("tw-box","^"));case"~":if(e.match("np~"))return o(t("meta","~/np~"))}if(a)switch(u){case"!":return e.match("!!!!!")||e.match("!!!!")||e.match("!!!")||e.match("!!"),o(n("header string"));case"*":case"#":case"+":return o(n("tw-listitem bracket"))}return null}var i,o,a,u,c=e.indentUnit;function f(e,t){var n=e.next(),i=e.peek();return"}"==n?(t.tokenize=r,"tag"):"("==n||")"==n?"bracket":"="==n?(o="equals",">"==i&&(e.next(),i=e.peek()),/[\'\"]/.test(i)||(t.tokenize=l()),"operator"):/[\'\"]/.test(n)?(t.tokenize=s(n),t.tokenize(e,t)):(e.eatWhile(/[^\s\u00a0=\"\'\/?]/),"keyword")}function s(e){return function(t,n){for(;!t.eol();)if(t.next()==e){n.tokenize=f;break}return"string"}}function l(){return function(e,t){for(;!e.eol();){var n=e.next(),r=e.peek();if(" "==n||","==n||/[ )}]/.test(r)){t.tokenize=f;break}}return"string"}}function k(){for(var e=arguments.length-1;e>=0;e--)a.cc.push(arguments[e])}function d(){return k.apply(null,arguments),!0}function p(e,t){var n=a.context&&a.context.noIndent;a.context={prev:a.context,pluginName:e,indent:a.indented,startOfLine:t,noIndent:n}}function m(){a.context&&(a.context=a.context.prev)}function g(e){if("openPlugin"==e)return a.pluginName=i,d(b,x(a.startOfLine));if("closePlugin"==e){var t=!1;return a.context?(t=a.context.pluginName!=i,m()):t=!0,t&&(u="error"),d(h(t))}return"string"==e?(a.context&&"!cdata"==a.context.name||p("!cdata"),a.tokenize==r&&m(),d()):d()}function x(e){return function(t){return"selfclosePlugin"==t||"endPlugin"==t?d():"endPlugin"==t?(p(a.pluginName,e),d()):d()}}function h(e){return function(t){return e&&(u="error"),"endPlugin"==t?d():k()}}function b(e){return"keyword"==e?(u="attribute",d(b)):"equals"==e?d(v,b):k()}function v(e){return"keyword"==e?(u="string",d()):"string"==e?d(z):k()}function z(e){return"string"==e?d(z):k()}return{startState:function(){return{tokenize:r,cc:[],indented:0,startOfLine:!0,pluginName:null,context:null}},token:function(e,t){if(e.sol()&&(t.startOfLine=!0,t.indented=e.indentation()),e.eatSpace())return null;u=o=i=null;var n=t.tokenize(e,t);if((n||o)&&"comment"!=n)for(a=t;!(t.cc.pop()||g)(o||n););return t.startOfLine=!1,u||n},indent:function(e,t){var n=e.context;if(n&&n.noIndent)return 0;for(n&&/^{\//.test(t)&&(n=n.prev);n&&!n.startOfLine;)n=n.prev;return n?n.indent+c:0},electricChars:"/"}})),e.defineMIME("text/tiki","tiki")}(n(46))}}]);
//# sourceMappingURL=107.193117df.chunk.js.map