import { 
    View, 
    Text, 
    SafeAreaView,
     Image, 
     TouchableOpacity,
     TextInput,
     ScrollView
     } from 'react-native'
import React from 'react'
import {
    AdjustmentsVerticalIcon,
     TrashIcon
} from "react-native-heroicons/solid"
import { SvgXml } from 'react-native-svg';
import categories from "../data/category"

// search icons 

const SearchIcon =
<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth={1.5} stroke="currentColor" className="size-6">
  <path strokeLinecap="round" strokeLinejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 5.196a7.5 7.5 0 0 0 10.607 10.607Z" />
</svg>

;

export default function HomeScreen() {
  return (
    <>
    <SafeAreaView className=" bg-white">
        <view className=" bg-white">
        <view className=" mt-2 mb-3 mx-4 flex-row items-center justify-between space=x=2">
<TouchableOpacity>
    <Image source={require("../assets/imgs/prof.png")} className= 
    " w-14 h-14 object-cover rounded-full"
     resizeMode="contain"
    />
</TouchableOpacity>
<view className=" flex-1">
    <Text className="text-lg font-bold text-black">
        Welcome Mystic!
    </Text>
    <Text className="font-light text-gray-500 text-xs">
        Nairobi-Karen
    </Text>
</view>
<TouchableOpacity className=" flex items-center justify-center bg-gray-400 rounded-full p-3">
<Text className="text-xs font-semibold absolute top=0 text-red-600">
    0
</Text>
<TrashIcon size={24} color="black"/>
</TouchableOpacity>
</view>
<view className=" mx-4 mt-2 mb-3">
<Text className=" text-4xl font-thin text-black">Order Your</Text>
<Text className=" text-4xl font-extrabold text-black">
Favorite Food
</Text>
</view>
<view className=" mx-4 mt-2 mb-3">
<TouchableOpacity className=" absolute z-50 top-[8px] left-[7px]">
<SvgXml xml={SearchIcon} color="gray" width={26} height={26}/>
</TouchableOpacity>
    <TextInput
    keyboardType="default"
    placeholder="Search Restaurants and Dishes"
    className=" p-3 rounded-xl bg-gray-400 shadow-lg placeholder:px-10 "
    />
    <TouchableOpacity className=" absolute z-50 top-[8px] right-[6px] border-l border-gray-400 px-1">
        <AdjustmentsVerticalIcon color="black" size={26}/>
    </TouchableOpacity>
</view>
 </view>
    </SafeAreaView>
    <ScrollView vertical showsVerticalScrollIndicator={false}>
    {/*categories*/}
    <view className=" mt-2">
    <view className=" mx-4">
     <Text className="  text[#f19c13] text-lg font-bold">
    Categories
    </Text>
    </view>
   
    </view>
    </ScrollView>
    </>
  )
}
