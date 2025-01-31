package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

// Git コマンドを生成する関数
func generateGitCommands(issueNumber int, issueTitle string) string {
	// タイトルを小文字に変換し、スペースをアンダースコアに置き換え
	formattedTitle := strings.ToLower(strings.ReplaceAll(issueTitle, " ", "_"))
	branchName := fmt.Sprintf("feature/#%d_%s", issueNumber, formattedTitle)

	// Git コマンドの出力
	commands := fmt.Sprintf(`git checkout -b %s
git commit -m "[%d] %s"
git push origin %s`, branchName, issueNumber, issueTitle, branchName)

	return commands
}

// ユーザー入力を処理する関数
func parseInput(input string) (int, string, error) {
	// 入力をトリムして不要なスペースを削除
	input = strings.TrimSpace(input)

	// "13. Roman to Integer" のような形式で split
	parts := strings.SplitN(input, ". ", 2)
	if len(parts) != 2 {
		return 0, "", fmt.Errorf("invalid input format. Expected format: '13. Roman to Integer'")
	}

	// issue_number を整数に変換
	issueNumber, err := strconv.Atoi(parts[0])
	if err != nil {
		return 0, "", fmt.Errorf("invalid issue number: %s", parts[0])
	}

	// issue_title を取得
	issueTitle := strings.TrimSpace(parts[1])

	return issueNumber, issueTitle, nil
}

func main() {
	// ユーザー入力の準備
	reader := bufio.NewReader(os.Stdin)

	// issue_number と issue_title の入力を受け取る
	fmt.Print("Enter issue (e.g., '13. Roman to Integer'): ")
	input, err := reader.ReadString('\n')
	if err != nil {
		fmt.Println("Error reading input.")
		return
	}

	// 入力の解析
	issueNumber, issueTitle, err := parseInput(input)
	if err != nil {
		fmt.Println("Error:", err)
		return
	}

	// Git コマンドを生成して出力
	fmt.Println(generateGitCommands(issueNumber, issueTitle))
}
