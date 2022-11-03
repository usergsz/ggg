local ip = "127.0.0.1"
local port = 4001
local err=0
local socket

function start()
	err,socket = TCPCreate(false,ip,port)
	print("err:")
	print(err)
	if err==0 then
		err = TCPStart(socket, 0)
		print(err)
	end
end
