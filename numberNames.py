'''
Number Names - Show how to spell out a number in English.
'''

numeral = {'0': '',
           '1': 'one',
           '2': 'two',
           '3': 'three',
           '4': 'four',
           '5': 'five',
           '6': 'six',
           '7': 'seven',
           '8': 'eight',
           '9': 'nine'
           }

digit_10 = {'2': 'twenty',
            '3': 'thirty',
            '4': 'forty',
            '5': 'fifty',
            '6': 'sixty',
            '7': 'seventy',
            '8': 'eighty',
            '9': 'ninety'
            }

exceptions = {'10': 'ten',
              '11': 'eleven',
              '12': 'twelve',
              '13': 'thirteen',
              '14': 'fourteen',
              '15': 'fifteen',
              '16': 'sixteen',
              '17': 'seventeen',
              '18': 'eighteen',
              '19': 'nineteen'
              }

group = {0: '',
         1: 'thousand',
         2: 'million',
         3: 'billion',
         4: 'trillion'
         }


def spell(num):

    if not isinstance(num, int):
        return 'Error! Wrong input type'

    result = ''
    st = ''
    sign = ''

    # Check for minus, sign is added to the output of the function
    s_num = str(num)
    if s_num[0] == '-':
        s_num = s_num[1:]
        sign = 'minus '

    # Splits number in groups of three number (thousands, millions, etc.) form end to start
    n=3
    nums = [s_num[-i-n:len(s_num)-i] for i in range(0, len(s_num), n)]

    if nums[0] == '0': return 'zero'

    # Iterate through groups of three and spelling them,
    # adding after each of them corresponding group name (thousand, millions etc.)
    # Result string is formed from end to start
    for i in range(0, len(nums)):
        if len(nums[i]) == 3:
            st = numeral[nums[i][0]] + ' hundred '
            nums[i] = nums[i][1:]
        if len(nums[i]) == 2:
            if nums[i] in exceptions:
                result = st + exceptions[nums[i]] + ' ' + group[i] + ' ' + result
                st = ''
                continue
            st = st + digit_10[nums[i][0]] + ' '
            nums[i] = nums[i][1:]
        result = st + numeral[nums[i][0]] + ' ' + group[i] + ' ' + result
        st = ''

    return sign + result
