# -*- coding: utf-8 -*-
"""
Created on Thu May 14 11:54:43 2020

@author: ashutosh.yadav
"""

import js2py
code1 = '''function getTypos(str) {
 
    //http://stackoverflow.com/questions/1431094/how-do-i-replace-a-character-at-a-particular-index-in-javascript
    String.prototype.replaceAt=function(index, char) {
	    return this.substr(0, index) + char + this.substr(index+char.length);
    }

    //define proximity arrays
    var array_prox = [];
    array_prox['a'] = ['q', 'w', 'z', 'x'];
    array_prox['b'] = ['v', 'f', 'g', 'h', 'n'];
    array_prox['c'] = ['x', 's', 'd', 'f', 'v'];
    array_prox['d'] = ['x', 's', 'w', 'e', 'r', 'f', 'v', 'c'];
    array_prox['e'] = ['w', 's', 'd', 'f', 'r'];
    array_prox['f'] = ['c', 'd', 'e', 'r', 't', 'g', 'b', 'v'];
    array_prox['g'] = ['r', 'f', 'v', 't', 'b', 'y', 'h', 'n'];
    array_prox['h'] = ['b', 'g', 't', 'y', 'u', 'j', 'm', 'n'];
    array_prox['i'] = ['u', 'j', 'k', 'l', 'o'];
    array_prox['j'] = ['n', 'h', 'y', 'u', 'i', 'k', 'm'];
    array_prox['k'] = ['u', 'j', 'm', 'l', 'o'];
    array_prox['l'] = ['p', 'o', 'i', 'k', 'm'];
    array_prox['m'] = ['n', 'h', 'j', 'k', 'l'];
    array_prox['n'] = ['b', 'g', 'h', 'j', 'm'];
    array_prox['o'] = ['i', 'k', 'l', 'p'];
    array_prox['p'] = ['o', 'l'];
    array_prox['r'] = ['e', 'd', 'f', 'g', 't'];
    array_prox['s'] = ['q', 'w', 'e', 'z', 'x', 'c'];
    array_prox['t'] = ['r', 'f', 'g', 'h', 'y'];
    array_prox['u'] = ['y', 'h', 'j', 'k', 'i'];
    array_prox['v'] = ['', 'c', 'd', 'f', 'g', 'b'];    
    array_prox['w'] = ['q', 'a', 's', 'd', 'e'];
    array_prox['x'] = ['z', 'a', 's', 'd', 'c'];
    array_prox['y'] = ['t', 'g', 'h', 'j', 'u'];
    array_prox['z'] = ['x', 's', 'a'];
    /*
    array_prox['1'] = ['q', 'w'];
    array_prox['2'] = ['q', 'w', 'e'];
    array_prox['3'] = ['w', 'e', 'r'];
    array_prox['4'] = ['e', 'r', 't'];
    array_prox['5'] = ['r', 't', 'y'];
    array_prox['6'] = ['t', 'y', 'u'];
    array_prox['7'] = ['y', 'u', 'i'];
    array_prox['8'] = ['u', 'i', 'o'];
    array_prox['9'] = ['i', 'o', 'p'];
    array_prox['0'] = ['o', 'p'];*/

    var arr = [];

	for(var a=0; a<str.length; a++) {
	    var temp = array_prox[str.charAt(a)];    
		for(var b=0; b<temp.length; b++) {
		    var typo = str.replaceAt(a, temp[b]);
		    arr.push(typo);
		}
	}

	return arr;
}'''
        
getTypos = js2py.eval_js(code1)
input_list= ['category','value', 'volume'] 
output_list= []
for i in range(len(input_list)):       
    output_list.append(getTypos(input_list[i]))

dict1 = {}
for i in range(len(output_list)):
    for j in range (len(output_list[i])):
        print(output_list[i][j])
        dict1[output_list[i][j]] = input_list[i]

        
#d = dict(zip(output_list,input_list)) 

     