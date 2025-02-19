package leetcodereview

func romanToInt(s string) int {
	var result, previousValue, currentValue int
	romanMap := map[uint8]int{
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000,
	}

    for i := len(s) - 1; i >= 0; i-- {
		currentValue = romanMap[s[i]]
		if currentValue < previousValue {
			result -= currentValue
		} else {
			result += currentValue
		}
		previousValue = currentValue
	}

	return result
}
