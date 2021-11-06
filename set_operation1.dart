void main(List<String> args) {
  var x =<int> {12,46,55,100};
  var y=<int> {19,55,33,1};
  var z=<int> {19,100,44,221};

  print("Example of set operation in the set :)");

  print("Union :)");

  print(x.union(y));

  print("Intersection :)");

  print(x.intersection(z));

  print("Difference :)");

  print(y.difference(z));
}