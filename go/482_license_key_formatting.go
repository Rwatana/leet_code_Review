package leetcodereview

import (
	"strings"
)

func cleanAndFormat(licenseKey string) string {
	licenseKey = strings.ReplaceAll(licenseKey, "-", "")
	return strings.ToUpper(licenseKey)
}

func insertSeparators(formattedKey string, groupSize int) string {
	if len(formattedKey) == 0 || groupSize <= 0 {
		return formattedKey
	}

	var result strings.Builder
	mod := len(formattedKey) % groupSize
	if mod == 0 {
		mod = groupSize
	}

	result.WriteString(formattedKey[:mod])
	for i := mod; i < len(formattedKey); i += groupSize {
		result.WriteString("-")
		end := i + groupSize
		if end > len(formattedKey) {
			end = len(formattedKey)
		}
		result.WriteString(formattedKey[i:end])
	}

	return result.String()
}

func licenseKeyFormatting(licenseKey string, groupSize int) string {
	cleanedKey := cleanAndFormat(licenseKey)
	return insertSeparators(cleanedKey, groupSize)
}