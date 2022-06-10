from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

class S(BaseHTTPRequestHandler):

	def _set_headers(self):

		self.send_response(400)
		self.send_header('Content-type', 'text/html')
		self.end_headers()

	def do_GET(self):

		#response
		self._set_headers()
		self.wfile.write("<html><body><h1>GET message receive!</h1></body></html>")

		if self.headers.get('Host')=='rwrgyme.shop:8081':
			#log
			print('-------------------------------------')
			print('Method: '+self.command)
			print('Host: '+self.headers.get('Host'))
			print('Address: '+self.address_string())
			print('-------------------------------------\r\n')

	def do_POST(self):

		self._set_headers()
		self.wfile.write("<html><body><h1>POST message receive!</h1></body></html>")

		#log
		print('-------------------------------------')
		print('Method: '+self.command)
		print('Host: '+self.headers.get('Host'))
		print('Content-Length: '+self.headers.get('Content-Length'))
		print('Content-Type: '+self.headers.get('Content-Type'))
		print('Address: '+self.address_string())

		content_len = int(self.headers.getheader('content-length', 0))
		print(self.rfile.read(content_len))
		print('-------------------------------------\r\n')


def run_http_server(server_class=HTTPServer, handler_class=S, port=8081):

	# startup HTTP server
	server_address = ('', port)
	httpd = server_class(server_address, handler_class)
	print('HTTP server started....')
	httpd.serve_forever()

if __name__ == '__main__':

	run_http_server()
