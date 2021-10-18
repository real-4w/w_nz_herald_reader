
Func = open("nz_h_p.html","w")
  
# Adding input data to the HTML file
Func.write("<html>\n<head>\n<title> \nOutput Data in an HTML file\n \
           </title>\n</head> <body> <h1>Welcome to \
           <font color = #00b300>NZ Herald Premium Reader</font></h1>\n \
           <h2>Premium news the cheap way</h2>\n</body></html>")

# Saving the data into the HTML file
Func.close()
Func = open("nz_h_p.html","a")
Func.write("Lalala.")  