#!/bin/bash

# Health
if curl --location --request GET 'https://nandini.duckdns.org/health' | grep -q ''; then echo "success"
else echo curl --location --request GET 'https://nandini.duckdns.org/health'
fi

# Register
if curl -X POST -d "username=nand.v&password=1234" 'https://nandini.duckdns.org/register' | grep -q 'User nand.v created successfully'; then echo "success"
else echo "error"
fi

if curl -X POST -d "username=nand.v" 'https://nandini.duckdns.org/register' | grep -q 'Password is required'; then echo "success"
else echo "error"
fi

# Login
if curl -X POST -d "username=nand.v&password=1234" 'https://nandini.duckdns.org/login' | grep -q 'Login Successful'; then echo "success"
else echo "error"
fi

if curl -X POST -d "username=nand.v&password=oof" 'https://nandini.duckdns.org/login' | grep -q 'Incorrect password'; then echo "success"
else echo "error"
fi
