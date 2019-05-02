import os
def Main():
	message = input("-> ")
	while message!='exit':
		if message=='TCP':
			os.startfile("Server.exe")
			os.startfile("Client.exe")
		elif message=='Basic_Connection':
			os.startfile("ServerBasic.exe")
			os.startfile("ClientBasic.exe")
		elif message=='Proxy_Basics':
			os.startfile("proxyServer.exe")
			os.startfile("prClient.exe")
			os.startfile("prServer.exe")
		elif message=='One_Server-multi_Client':
			os.startfile("threadingServer.exe")
			os.startfile("threadingClient1.exe")
			os.startfile("threadingClient2.exe")
		elif message=='Cookie_Analyzer':
			os.startfile("cookieanalizer.exe")
		elif message=='Header_Analyzer':
			os.startfile("headeranalizer.exe")
		message = input("-> ")
if __name__ == '__main__':
    Main()