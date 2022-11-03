local code_num = 0

function main()
	local err = 0
	local A_result
	local B_result
	local ProductPos = {}
	err,A_result,B_result,ProductPos = receive()
	if A_result == "set" then
		code_num = code_num+1
		if code_num == 1 then
			Jump(P2, "Start=200, ZLimit=200, End=208, SYNC=1")
		elseif code_num == 2 then
			Jump(P3, "Start=200, ZLimit=200, End=200, SYNC=1")
		elseif code_num == 3 then
			Jump(P4, "Start=200, ZLimit=200, End=200, SYNC=1")
		elseif code_num == 4 then
			Jump(P5, "Start=200, ZLimit=200, End=200, SYNC=1")
		elseif code_num == 5 then
			Jump(P6, "Start=208, ZLimit=208, End=208, SYNC=1")
		elseif code_num == 6 then
			Jump(P7, "Start=208, ZLimit=208, End=208, SYNC=1")
		end
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("ok1")
	elseif A_result == "return" then
		Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		if code_num == 1 then
			Jump(P2, "Start=208, ZLimit=208, End=208, SYNC=1")
		elseif code_num == 2 then
			Jump(P3, "Start=208, ZLimit=208, End=208, SYNC=1")
		elseif code_num == 3 then
			Jump(P4, "Start=208, ZLimit=208, End=208, SYNC=1")
		elseif code_num == 4 then
			Jump(P5, "Start=208, ZLimit=208, End=208, SYNC=1")
		elseif code_num == 5 then
			Jump(P6, "Start=208, ZLimit=208, End=208, SYNC=1")
		elseif code_num == 6 then
			Jump(P7, "Start=208, ZLimit=208, End=208, SYNC=1")
		end
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("ok2")
	
	if B_result == "A1" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P9, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("ok2")
	elseif B_result == "B1" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P10, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("ok2")
	elseif B_result == "C1" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P11, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("ok2")
	elseif B_result == "D1" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P12, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("ok2")
	elseif B_result == "A2" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P9, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("again")
	elseif B_result == "B2" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P10, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("again")
	elseif B_result == "C2" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P11, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("again")
	elseif B_result == "D2" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P12, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("again")
	elseif B_result == "F2" then
	    Jump(P8, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,1)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		Jump(P13, "Start=208, ZLimit=208, End=208, SYNC=1")
		DO(1,0)
		Jump(P1, "Start=208, ZLimit=208, End=208, SYNC=1")
		send("again")
	end
    A_result = nil
	B_result = nil
	end
end

start()
Go(P1,"SYNC=1")
DO(1,0)
while true do
	main()
end