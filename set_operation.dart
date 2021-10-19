void main(List<String> args) {
  var x=<int>{12,34,45,55};
  var y=<int>{11,34,44,78};
  print("Set operations: ");
  print("union of x and y ");
  print(x.union(y));
  print("intersection of x and y ");
  print(x.intersection(y));
  print("y difference x :");
  print(y.difference(x));
}