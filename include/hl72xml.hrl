-define(TCP_OPTIONS, [binary, {packet, 0}, {active, true}, {reuseaddr, true}]).
-define(SPLIT(Str,Exp),re:split(Str,Exp,[{return,list},trim])).  
-define(DEL_SEGMENT,"[\n]").          
-define(DEL_FIELD,"[\|]").          
-define(DEL_COMPONENT,"[\\^]"). 	    
-define(DEL_SUBCOMPONENT,"[\&]").          
-define(DEL_REPEAT_FIELD,"[\~]").  	    
-define(ENCODING,"^~&").  
-define(TYPES,["segments","header","fields","components","subcomponents"]).