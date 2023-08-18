package main

import (
	"fmt"
)

// list node
type SingleNode struct {
	val int // value of node
	Next *SingleNode // pointer of next node 
}

// linkList
type LinkList struct {
	dummyHead *SingleNode
	size int
}

// initialize the dummy head
func Constructor() LinkList { 
	newNode := &SingleNode{
		val: -999,
		Next: nil,
	}

	return LinkList{
		dummyHead: newNode,
		size: 0,
	}
}

func (l *LinkList) Get(index int) int {
	if l == nil || index < 0 || index > l.size {
		return -1
	}
	cur := l.dummyHead.Next

	for i:=0; i < index; i++ {
		cur = cur.Next
	}
	return cur.val
}

func (l *LinkList) AddAtHead(val int) {
	newNode := &SingleNode{
		val: val,
	}
	newNode.Next = l.dummyHead.Next 
	l.dummyHead.Next = newNode
	l.size ++
}

func (l *LinkList)AddAtTail(val int) {
	newNode := &SingleNode{
		val: val,
	}

	position := l.size
	cur := l.dummyHead
	for i:=0; i < position; i++ {
		cur = cur.Next
	}

	cur.Next = newNode
	l.size ++
}

func (l *LinkList)AddAtIndex(val int, index int) {
	if index < 0 {
		index = 0
	} else if index > l.size {
		return 
	}
	newNode := &SingleNode{
		val: val,
	}
	cur := l.dummyHead
	for i :=0; i < index; i++ {
		cur = cur.Next 
	}
	newNode.Next = cur.Next 
	cur.Next = newNode
	l.size ++ 
}

func (l *LinkList)DeleteAtIndex(index int) {
		if index < 0 || index > l.size {
			return 
		}

		cur := l.dummyHead
		for i := 0; i < index; i++ {
			cur = cur.Next 
		}
		cur.Next = cur.Next.Next 
		l.size --
}

func (l *LinkList)printLinkedList(){
	cur := l.dummyHead
	for cur.Next != nil {
		fmt.Println(cur.val)
		cur = cur.Next 
	}
}

func main() {
	list := Constructor()     // 初始化链表
	list.AddAtHead(100)       // 在头部添加元素
	list.AddAtTail(242)       // 在尾部添加元素
	list.AddAtTail(777)       // 在尾部添加元素
	list.AddAtIndex(1, 99999) // 在指定位置添加元素
	list.printLinkedList()    // 打印链表
}