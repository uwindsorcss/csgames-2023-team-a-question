#! /usr/bin/csh

set arr = `grep " " input.txt`
set num_rows = `cat input.txt | grep  " " | wc -l`
set num_cols = `cat input.txt | head -n 1 | awk 'END {print NF}'`
echo $arr $num_rows $num_cols
#set nodes = ( `echo $arr | sed 's/_/ /g'` )
#echo $nodes
#set i = 1
#foreach letter ( $nodes )
#  set neighbor_list = ""
#  if ( $i > $num_cols ) then
#     set top = `expr $i -  $num_cols`
#     set neighbor_list = "${neighbor_list}_$nodes[$top]:$top"
#  endif
#  if ( $i <= `expr \( $num_rows - 1 \) * $num_cols` ) then 
#     set bottom = `expr $i + $num_cols`
#     set neighbor_list = "${neighbor_list}_$nodes[$bottom]:$bottom"
#  endif
#  if ( `expr $i % $num_cols` == 1 ) then 
#  if ( ! `expr $i % $num_cols` ) then
#end

set words = ( `grep -v " " input.txt` )
#echo $words
set i = 1
while ( $i <= $#words )
   set current_word = ( `echo $words[$i] | sed 's/ */ /g'` )
   set first_letter =  $current_word[1]
   set stack = ( `echo $arr | sed 's/ /\n/g' | grep -n $first_letter | sed 's/$/_1/g'` )
   set flag = 0
   set visited = ()
   #echo $stack
   while ( $#stack )
     set current = $stack[1]
     set current_pos = `echo $current | awk -F ':' '{print $1}'`
     if ( $current_pos == 1 ) then
        set visited = ()
     endif
     set visited = ( "$current_pos" "$visited")
     set current_letter = `echo $current | awk -F '_|:' '{print $2}' `
     set letter_position = `echo $current | awk -F '_' '{print $2}'`
     set next_letter_pos = `expr $letter_position + 1`
     set stack = `echo $stack[2-]`
     set neighbors = ()
     if ( $current_pos > $num_cols ) then
        set top = `expr $current_pos - $num_cols`
        set neighbors = ( $neighbors $top )
     endif
     if ( $current_pos <= `expr \( $num_rows - 1 \) \* $num_cols` ) then
        set bottom = `expr $current_pos + $num_cols`
        set neighbors = ( $neighbors $bottom )
     endif
     if ( `expr $current_pos % $num_cols` != 1 ) then
        set left = `expr $current_pos - 1`
        set neighbors = ( $neighbors $left )
     endif
     if ( `expr $current_pos % $num_cols` != 0 ) then 
        set right = `expr $current_pos + 1`
        set neighbors = ( $neighbors $right )
     endif
     foreach neighbor ( $neighbors )
        #echo $neighbor
        if ( ($arr[$neighbor] == $current_word[$next_letter_pos]) && (`echo $visited | sed 's/ /\n/g' | grep "^$neighbor"'$'` != $neighbor) ) then
           if ( $next_letter_pos == $#current_word ) then
              set flag = 1
           else
              set stack = ( "${neighbor}:$arr[$neighbor]_${next_letter_pos}" $stack )
           endif
        endif
     end
     #echo $stack
     if ( $flag ) then
        echo "True"
        break
     endif
   end
   if ( ! $flag ) then
      echo "False"
   endif
   @ i = ( $i + 1 )
end
