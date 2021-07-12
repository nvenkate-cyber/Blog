#!/bin/bash

# Health
if curl --location --request GET 'https://nandini.duckdns.org/health' | grep -q ''; then echo "success"
else echo "error"
fi

# Register
if curl -X POST -d "username=nand.v&password=1234" 'https://nandini.duckdns.org/register' | grep -q 'User nand created successfully'; then echo "success"
else echo "error"
fi

if curl -X POST -d "username=nandini.v" 'https://nandini.duckdns.org/' | grep -q 'Password is required'; then echo "success"
else echo "error"
fi

# Login
if curl -X POST -d "username=nand&password=1234" 'https://nandini.duckdns.org/login' | grep -q 'Login Successful'; then echo "success"
else echo "error"
fi

if curl -X POST -d "username=nandini.v&password=oof" 'https://nandini.duckdns.org/login' | grep -q 'Incorrect password'; then echo "success"
else echo "error"
fi
