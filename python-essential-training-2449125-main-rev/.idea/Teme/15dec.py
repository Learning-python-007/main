/* create 2 classes in python with main class */
class MainClass:
    constructor(name)
    this.name = name
    getName():
        return this.name

class SubClass extends MainClass {
constructor(name, age) {
super(name);
this.age = age;
}
getAge() {
return this.age;
}
}
var subClass = new SubClass('John', 20);
console.log(subClass.getName());
console.log(subClass.getAge());

/* create 2 classes in python */
class MainClass {
constructor(name) {
this.name = name;
}
getName() {
return this.name;
}
}
class SubClass extends MainClass {
constructor(name, age) {
super(name);
this.age = age;
}
getAge() {
return this.age;
}
}
var subClass = new SubClass('John', 20);
console.log(subClass.getName());
console.log(subClass.getAge());

/* , with static and private methods */
class MainClass {
constructor(name) {
this.name = name;
}
getName() {
return this.name;
}
}
class SubClass extends MainClass {
constructor(name, age) {
super(name);
this.age = age;
}
getAge() {
return this.age;
}
}
var subClass = new SubClass('John', 20);
console.log(subClass.getName());
console.log(subClass.getAge());