#js object basics
object is a collection of data and functions that are related
it can consist of :)variables -> properties
:)functions -> methods
#declare object (object literal)
const/let student = {}; (empty object)
let se = {
  name: Cheta, //property
  age: 24, //property
  sayHi: function () {
    console.log(`hi i am ${this.name}`);
  }, //method
  or
  sayHi() {
    console.log(`hi i am ${this.name}`);
  }, //method
  let stack = {
    low_level: "c",
    higher_level: "python",
  },//object as a property
};
"this" refers to the current object much like "self" in python
#accessing members
:) dot notation
	student.name;
:) braccket notation
	student["name"];
#setting members
:) dot notation
        student.name = "john";
	student.new = "a new property";
:) braccket notation
        student["name"] = "john";
the dot notation is generally prefered since it is more readable
#constructors
a constructor is a function called using tht new keyword it
:| creates a new object
:| bind this to the new object so "this" in the constructor would refer to it
:| run the code in the constructor 
:| return the created/constructed object

function Student(name) {
  this.name = name;
  this.sayHi = function () {
    console.log(`Hi I am ${this.name}`);
  };
}

#call constructor
const cheta = new Student("cheta");

#prototypes
a means for object to inherit features/properties from one another
every object in js has a built-in property known as prototype, the prototype being an object witha prototype, this leads to a  chain of prototypes the chain ends when the parent prototype is null "object.prototype" is at the head of this chain, hence every object in js inherits from it (its an ancestor of all object types).

when a property is accessed on an object by say
	student.name;
the property is first searched for in that object, if it is not found its prototype is searched, the search continues in that order untill the property is found or until the parent prototype is null in which case undefined is returned

#setting prototypes
:| Object.create()
:| constructors
