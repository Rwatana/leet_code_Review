package leetcodereview

// isIsomorphic checks if two strings are isomorphic.
// It returns true if characters in source can be replaced to get target with a one-to-one mapping.
func isIsomorphic(source, target string) bool {
	// If the lengths of the strings are different, they cannot be isomorphic.
    if len(source) != len(target) {
        return false
    }

    charMapST := make(map[byte]byte) // mapping from source's character to target's character
    charMapTS := make(map[byte]byte) // mapping from target's character to source's character

    for i := range source {
        charSource, charTarget := source[i], target[i]

        // check mapping from source to target
        if mappedTarget, foundTarget := charMapST[charSource]; !foundTarget {
            charMapST[charSource] = charTarget
        } else if mappedTarget != charTarget {
            return false
        }

        // check mapping from target to source
        if mappedSource, foundSource := charMapTS[charTarget]; !foundSource {
            charMapTS[charTarget] = charSource
        } else if mappedSource != charSource {
            return false
        }
    }

    return true
}
