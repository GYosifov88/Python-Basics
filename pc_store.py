procesor_price_dolars = float(input())
video_card_price_dolars = float(input())
ram_memory_price_dolars = float(input())
number_of_ram_memories = int(input())
discount_percent = float(input())

procesor_price_leva = procesor_price_dolars * 1.57
video_card_price_leva = video_card_price_dolars * 1.57
ram_memory_price_leva = ram_memory_price_dolars * 1.57

total_ram_cost = ram_memory_price_leva * number_of_ram_memories
price_procesor_after_discount = procesor_price_leva - (procesor_price_leva * discount_percent )
video_card_after_discount = video_card_price_leva - (video_card_price_leva * discount_percent )

total_cost = total_ram_cost + price_procesor_after_discount + video_card_after_discount

print(f'Money needed - {total_cost:.2f} leva.')