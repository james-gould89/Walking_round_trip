locations = ["office", "gateway 1000 roundabout", "petral station", "ford roundabout", "BMW", "The IO centre", "whittle Way/ gunnels wood Road", "gunnels wood/Broadhal Way roundabout", "gunnels underpass - whittle way","gunnels underpass - N&C", "gunnels underpass - LB Electrics", "gunnels wood park", "football club roundabout", "retail park - M&S", "Fairlands Valley park"]

values = {"office":0, "gateway 1000 roundabout":1, "petral station":2, "ford roundabout":1, "BMW":2, "The IO centre":1, "whittle Way/ gunnels wood Road":2, "gunnels wood/Broadhal Way roundabout":2, "gunnels underpass - whittle way":3,"gunnels underpass - N&C":2, "gunnels underpass - LB Electrics":3, "gunnels wood park":2, "football club roundabout":3, "retail park - M&S":4, "Fairlands Valley park":20 }

connections = [["office", "gateway 1000 roundabout", 1], 
               ["gateway 1000 roundabout", "petral station",1],
               ["gateway 1000 roundabout", "ford roundabout",2],
               ["gateway 1000 roundabout", "BMW", 2],
               ["gateway 1000 roundabout", "The IO centre", 3],
               ["ford roundabout", "BMW", 1],
               ["ford roundabout", "The IO centre", 3],
               ["ford roundabout", "whittle Way/ gunnels wood Road", 1],
               ["whittle Way/ gunnels wood Road","petral station", 2], 
               ["whittle Way/ gunnels wood Road", "gunnels underpass - whittle way", 1],
               ["whittle Way/ gunnels wood Road", "gunnels wood/Broadhal Way roundabout", 3],
               ["whittle Way/ gunnels wood Road", "gunnels underpass - N&C", 5],
               ["whittle Way/ gunnels wood Road", "gunnels underpass - LB Electrics", 11],
               ["gunnels underpass - whittle way", "gunnels underpass - N&C", 5],
               ["gunnels underpass - whittle way", "gunnels underpass - LB Electrics", 11],
               ["gunnels underpass - whittle way", "gunnels wood park", 8],
               ["gunnels underpass - whittle way", "gunnels wood/Broadhal Way roundabout", 3],
               ["gunnels underpass - N&C", "gunnels wood park", 5],
               ["gunnels underpass - N&C", "gunnels underpass - LB Electrics", 5],
               ["gunnels underpass - N&C", "gunnels wood/Broadhal Way roundabout", 11],
               ["gunnels underpass - LB Electrics","gunnels wood park", 3],
               ["gunnels underpass - LB Electrics", "gunnels wood/Broadhal Way roundabout", 15],
               ["gunnels wood/Broadhal Way roundabout", "petral station", 1],
               ["gunnels wood/Broadhal Way roundabout", "football club roundabout", 5],
               ["gunnels wood/Broadhal Way roundabout", "retail park - M&S", 8],
               ["retail park - M&S", "football club roundabout", 3],
               ["football club roundabout", "Fairlands Valley park", 8]
               ]