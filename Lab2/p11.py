def order_tuples(tuple_list):
    tuple_list.sort(key=lambda tup:tup[1][2])#sorteaza in fuctie de a 2 a valoare caract al 3 lea(google)
    return tuple_list

if __name__=='__main__':
  a=[("abc","bcd"),("abc","zza")]
  print(order_tuples(a))