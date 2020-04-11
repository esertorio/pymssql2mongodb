function toPrint(data) {
  print(JSON.stringify(data, null, 2));
}

toPrint(db.ColecaoUm.find());
