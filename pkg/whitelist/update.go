package whitelist

import (
	"fmt"
	"io/ioutil"
	"os"
	"path"
	"regexp"
)

func DeleteIPFromWhiteList(filePath, ip string) error {
	f, err := ioutil.ReadFile(filePath)
	if err != nil {
		fmt.Println("open files failed.")
		return err
	}
	contents := string(f)
	r := regexp.MustCompile(ip + "\n")
	fmt.Println(r)
	newContents := r.ReplaceAllString(contents, "")
	fmt.Println(newContents)
	_, err = writeString(filePath, newContents)
	if err != nil {
		fmt.Println("write files failed.")
		return err
	}
	return nil

}

func writeBytes(filePath string, b []byte) (int, error) {
	os.MkdirAll(path.Dir(filePath), os.ModePerm)
	fw, err := os.Create(filePath)
	if err != nil {
		return 0, err
	}
	defer fw.Close()
	return fw.Write(b)
}

func writeString(filePath string, s string) (int, error) {
	return writeBytes(filePath, []byte(s))
}
