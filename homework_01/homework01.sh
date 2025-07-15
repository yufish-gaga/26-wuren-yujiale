#生成目录结构和文件
mkdir -p linux_practice/name
mkdir -p linux_practice/permission
touch linux_practice/name/file1.txt
touch linux_practice/name/file2.txt
touch linux_practice/permission/file3.txt
touch linux_practice/permission/file4.txt

#删除file1.txt
rm -f linux_practice/name/file1.txt

#改名
mv linux_practice/name/file2.txt linux_practice/name/show.txt

#修改内容
echo "Hello linux" > linux_practice/name/show.txt

#输出内容
cat linux_practice/name/show.txt

#修改文件权限和输出信息
for file in linux_practice/permission/file3.txt linux_practice/permission/file4.txt; do
	chmod 644 "$file"
	echo "Changed permissions for $(basename "$file") to -rw-r--r--"
done
