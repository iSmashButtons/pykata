Notes and useful information I've found while working through these katas.

# Number Formatting

Source: [makz.blog Python String Format Cookbook](https://mkaz.blog/code/python-string-format-cookbook/)

The following table shows various ways to format numbers using Python’s str.format(), including examples for both float formatting and integer formatting.

To run examples use: `print("FORMAT".format(NUMBER))`

To get the output of the first example, formatting a float to two decimal places, you would run:

`print("{:.2f}".format(3.1415926))`

|Number|Format|Output|Description|
|------|------|------|------|
|3.1415926|{:.2f}|3.14|Format float 2 decimal places|
|3.1415926|{:+.2f}|+3.14|Format float 2 decimal places with sign|
|-1|{:+.2f}|-1.00|Format float 2 decimal places with sign|
|2.71828|{:.0f}|3|Format float with no decimal places|
|5|{:0>2d}|05|Pad number with zeros (left padding, width 2)|
|5|{:x<4d}|5xxx|Pad number with x’s (right padding, width 4)|
|10|{:x<4d}|10xx|Pad number with x’s (right padding, width 4)|
|1000000|{:,}|1,000,000|Number format with comma separator|
|0.25|{:.2%}|25.00%|Format percentage|
|1000000000|{:.2e}|1.00e+09|Exponent notation|
|13|{:10d}|        13|Right aligned (default, width 10)|
|13|{:<10d}|13|Left aligned (width 10)|
|13|{:^10d}|    13|Center aligned (width 10)|