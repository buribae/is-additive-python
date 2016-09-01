is-additive-python
==========================
Determines if function(x+y) = function(x) + function(y)

#### Python Environment
version: Python 2.7.12

os: OSX El Capitan 10.11.6

#### How to run this repo
```sh
# 1) clone this repository
git clone https://github.com/buribae/is-additive-python.git

# 2) open terminal. Move into the folder
cd \{Path}

# 3) enter following command example:
python is_additive.py {argument}

```

#### Accepted Argument
- is_additive.py only accepts only one first argument as the input.
- Only integer type works for input.

##secret(x)
==========================
You can also change secret(x) to see different results.
@Define Additive: secret(x+y) = secret(x) + secret(y)
Example:
(secret(x): return x) is additive
(secret(x): return x+x) is additive
