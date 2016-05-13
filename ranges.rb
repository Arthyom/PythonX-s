telefono = "t313f0no"
mth = /%[09]%/
r = mth.match(telefono)
unless r
	puts "no"
	else
		puts r	
end
