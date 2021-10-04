import random
import time

chip =int(input('お互いのチップは何枚にしますか？：'))
p1_chip = chip
p2_chip = chip
ante = int(input('参加費は何枚にしますか？：'))
betsize = int(input('ベットサイズは何枚にしますか？：'))
p1_name = input('名前を入力してください：')
p2_name = 'コンピュータ'
time.sleep(0.5)
print('対戦相手は' + p2_name + 'です')
count = int(input('何回勝負しますか？：'))
print('')

for i in range(1, count + 1):
  card_list1 = []
  card_list2 = []
  for number in range(1, 4):
    if number == 1:
      card = 'Q'
      card_list1.append(card)
    elif number == 2:
      card = 'K'
      card_list2.append(card)
    else:
      card = 'A'
      card_list1.append(card)

  random.shuffle(card_list1)
  oop_card = card_list1.pop(0)
  ip_card = card_list2.pop(0)
  pot_chip = 0
  time.sleep(1)

  print(str(i) + '回目の勝負を始めます。')
  time.sleep(1)
  print(p1_name + 'の現在のチップの量は' + str(p1_chip) + '枚です。')
  time.sleep(1)
  print(p1_name + 'と' + p2_name + 'からそれぞれ' + str(ante) + '枚の参加費を貰いました。')
  p1_chip -= ante
  p2_chip -= ante
  pot_chip += ante *2
  print('現在のポットに入っている枚数は' + str(pot_chip) + '枚です。')
  oop_odds = round(betsize / (pot_chip + betsize), 2)
  ip_odds = round(betsize / (betsize * 2 + pot_chip), 2)
  freq1 = random.randint(1, 101)
  freq2 = random.randint(1, 101)
  time.sleep(1)

  #奇数回目
  if i % 2 != 0:
    print(p1_name + 'が攻め、' + p2_name + 'が受けになります。')
    time.sleep(1)
    print(p1_name + 'に' + oop_card + 'が配られました。')
    time.sleep(1)
    print('乱数は' + str(freq1) + 'でした。')
    time.sleep(1)

    #p1_nameのアクション
    if 0 < freq1 <= oop_odds * 100:
      print('ベットを選択してください。')
    else:
      print('Aはベット、Qはチェックを選択してください。')
    time.sleep(1)
    oop_act = input('アクションを選択してください。　b：ベット　or　x：チェック：')

    #p2_nameのアクション　
    if 0 < freq2 <= ip_odds * 100:
      ip_act = 'c'
    else:
      ip_act = 'f'

    #勝負
    time.sleep(1)
    if oop_card == 'A':
      if oop_act == 'b' and ip_act == 'c':
        p1_chip += pot_chip + betsize
        p2_chip -= betsize
        print(p1_name + 'は２枚ベット。')
        time.sleep(1)
        print(p2_name + 'はコール。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はA、' + p2_name + 'はK。')
        time.sleep(1)
        print(p1_name + 'の勝ち！')
      elif oop_act == 'b' and ip_act =='f':
        p1_chip += pot_chip
        print(p1_name + 'は2枚ベット。')
        time.sleep(1)
        print(p2_name + 'はフォールド。')
        time.sleep(1)
        print(p1_name + 'の勝ち！')
      else:
        print('お互いにチェック。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はA、' + p2_name + 'はK。')
        print(p1_name + 'の勝ち！')
    else:
      if oop_act == 'b' and ip_act == 'c':
        p1_chip -= betsize
        p2_chip += pot_chip + betsize
        print(p1_name + 'は２枚のベット。')
        time.sleep(1)
        print(p2_name + 'はコール。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はQ、' + p2_name + 'はK。')
        time.sleep(1)
        print(p2_name + 'の勝ち！')
      elif oop_act == 'b' and ip_act == 'f':
        p1_chip += pot_chip
        print(p1_name + 'は２枚のベット。')
        time.sleep(1)
        print(p2_name + 'はフォールド。')
        time.sleep(1)
        print(p1_name + 'の勝ち！')
      else:
        p2_chip += pot_chip
        print('お互いにチェック。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はQ、' + p2_name + 'はK。')
        time.sleep(1)
        print(p2_name + '勝ち！')

  #偶数回目
  else:
    print(p2_name + 'が攻め、' + p1_name + 'が受けになります。')
    time.sleep(1)
    print(p1_name + 'に' + ip_card + 'が配られました。')
    time.sleep(1)
    print('乱数は' + str(freq2) + 'でした。')
    time.sleep(1)

    #p2_nameのアクション
    if oop_card == 'A':
      oop_act = 'b'
    else:
      if 0 < freq1 <= oop_odds * 100:
        oop_act = 'b'
      else:
        oop_act = 'x'

    #p1_nameのアクション
    if 0 < freq2 <= ip_odds * 100:
      print('コールを選択してください。')
    else:
      print('フォールドを選択してください。')
    time.sleep(1)
    ip_act = input('アクションを選択してください。　c：コール　f：フォールド：')

    #勝負
    time.sleep(1)
    if oop_card == 'A':
      if oop_act == 'b' and ip_act == 'c':
        p2_chip += betsize + pot_chip
        p1_chip -= betsize
        print(p2_name + 'は' + str(betsize) + '枚のベット。')
        time.sleep(1)
        print(p1_name + 'はコール。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はK、' + p2_name + 'はA。')
        time.sleep(1)
        print(p2_name + 'の勝ち！')
      elif oop_act == 'b' and ip_act == 'f':
        p2_chip += pot_chip
        print(p2_name + 'は' + str(betsize) + '枚のベット。')
        time.sleep(1)
        print(p1_name + 'はフォールド。')
        time.sleep(1)
        print(p2_name + 'の勝ち！')
      else:
        p1_chip += pot_chip
        print('お互いにチェック。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はK、' + p2_name + 'はA。')
        time.sleep(1)
        print(p2_name + 'の勝ち！')
    else:
      if oop_act == 'b' and ip_act == 'c':
        p2_chip -= betsize
        p1_chip += betsize + pot_chip
        print(p2_name + 'は' + str(betsize) + '枚のベット。')
        time.sleep(1)
        print(p1_name + 'はコール。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はK、' + p2_name + 'はQ。')
        time.sleep(1)
        print(p1_name + 'の勝ち！')
      elif oop_act == 'b' and ip_act == 'f':
        p2_chip += pot_chip
        print(p2_name + 'は' + str(betsize) + '枚のベット。')
        time.sleep(1)
        print(p1_name + 'はフォールド。')
        time.sleep(1)
        print(p2_name + 'の勝ち！')
      else:
        p1_chip += pot_chip
        print('お互いにチェック。')
        time.sleep(1)
        print('SHOW DOWN')
        time.sleep(1)
        print(p1_name + 'はK、' + p2_name + 'はQ。')
        time.sleep(1)
        print(p1_name +'の勝ち！')

  #勝負後のお互いのチップ量
  time.sleep(1)
  print(p1_name + 'は現在' + str(p1_chip) + '枚のチップを保有しています。')
  time.sleep(1)
  print(p2_name + 'は現在' + str(p2_chip) + '枚のチップを保有しています。')
  print('')

#最終結果
time.sleep(1)
if p1_chip > p2_chip:
  print(p1_name + 'の勝ち！')
  print('！！！ビクトリーロイヤル！！！')
elif p1_chip == p2_chip:
  print('引き分け')
else:
  print(p2_name + 'の勝ち！')
  print('残念！')
