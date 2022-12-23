import os
from time import time
import binascii
import math
import os.path

lenf=0
name=""
add_bits=""
Make_togher=""


namez = input("c,  compress or e, extract? ")

#@Author Jurijus Pacalovas
class compression:
       
        def cryptograpy_compression4(self):
                
                self.name = "Written: Jurijus pacalovas"

                if namez!="c" and namez!="e":
                        print("The wrong letter")
                        raise SystemExit
                if namez=="c" or namez=="e":        
                    if namez=="c":

                        i=1

                    if namez=="e":
                        i=2
                 
                    Number_add_plus_one=""
                    Prime_Not=""
                    Times_6=""
                    Corrupted=0
                      
                    name = input("What is name of file? ")

                    if os.path.exists(name):
                            print('Path is exists!')
                    else:
                            print('Path is not exists!')
                            raise SystemExit

                    x=0
                    x1=0
                    x2=0
                    n=0
                    x = time()
                    
                            
                    
                    namem=""
                    namema="?"
        
                    nameas=name
                    nac=len(nameas)
                    
                    compress_or_not_compress=1
                    Circle_times3=0

                    if i==2:
                        if nameas[nac-4:nac]==".bin":
                   
                        	nameas=name[:nac-4]
                        	nac=len(nameas)
                        	
                        	C=1

                        elif nameas[nac-4:nac]!=".bin":
                                print("Sorry, this is not binary file!")
                                raise SystemExit
                   
                    if i==1:
                        
                        nameas=name+".bin"
                    
                    	
                    nac=len(nameas)
                    
                   
                    s=""

                    Equal_info_between_of_the_cirlce_of_the_file=""
                    Equal_info_between_of_the_cirlce_of_the_file_2=""

                  
                    Times_6=""

                    Translate_info_Decimal=""

                    D=0
                    

                    
                    
                        

                    
                                       
                    

                    with open(nameas, "w") as f4:
                            f4.write(s)
                    with open(nameas, "a") as f3:
                            f3.write(s)
                    with open(name, "rb") as binary_file:

                       # Read the whole file at once
                        data = binary_file.read()
                     
                            
                         
      
                        s=str(data)

                        lenf1=len(data)
                        lenf7=len(data)
                        if lenf7==0:
                        	 raise SystemExit
                        
                        END_working=0
                        Circle_times2=0
                                   
                        Equal_info_between_of_the_cirlce_of_the_file_23=""
 
                        sda18=""
                        Equal_info_between_of_the_cirlce_of_the_file_29=""
                        
                        SpinS=0
                        while END_working<10:
                       
                            Circle_times3=Circle_times3+1
                            D=1
                            if D==1:
                                if Circle_times3==1:

                                 
                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)
                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1
                                            
                                    

                                    if Circle_times3==1:
                                        Equal_info_between_of_the_cirlce_of_the_file_2=sda
                            
                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_2, 2)
                                
                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                    width_bits=(width_bits/8)*2
                                    width_bits=str(width_bits)
                                    width_bits="%0"+width_bits+"x"
                             
                                    width_bits3=binascii.unhexlify(width_bits % n)                                    
                                    width_bits2=len(width_bits3)
                                    
                                    data=width_bits3
                                  
                                    lenf5=len(data)

                                    sda=bin(int(binascii.hexlify(data),16))[2:]
                                    lenf=len(sda)

                                    lenf1=len(data)
                                
                                    count_bits=(lenf1*8)-lenf
                                    z=0
                                    if count_bits!=0:
                                        while z<count_bits:
                                            sda="0"+sda
                                            z=z+1

                                    Equal_info_between_of_the_cirlce_of_the_file_2=sda
                                   
                                    
                                    
                                    Extact=Equal_info_between_of_the_cirlce_of_the_file_2
                                    A=int(Extact,2)
                                    

                                    lenf3=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                lenf2=len(Equal_info_between_of_the_cirlce_of_the_file_2)
                                #print(lenf2)
                                if i==1:
                                    if lenf7>=(2**40)-1:
                                        raise SystemExit

                                #########################################################################################################################################################
                                
                                
                                if i==1:
                                    if  int(sda,2)==0:
                                                    long_of_file=len(sda)
                                                    
                                                    Nuber_zero_or_else=int(sda,2)
                                                    long_of_file+=1
                                                    #print(long_of_file)
                                                    if Nuber_zero_or_else==0 and long_of_file<(2**112):
                                                                                                 long_of_file_N=format(long_of_file,'08b')
                                                                                                 Compress_zeros=long_of_file_N
                                                                                             
                                    from qiskit.circuit import QuantumCircuit
                                    k1=0
                                    k2=1
                                    Y1=1
                                   
                                    circuit = QuantumCircuit(2002) 
                                    
                                    Extract1=0
                                    Times_10=1
                                    Times_7=0
                                    Times_11=-1
                                    
                                    N_5=-1
                                    

                                    while Extract1!=1:
                                        
                                        

                                           
                                            
                                            
                                            k1+=1
                                            k2+=1
                                            if k1==2000:
                                                k1=0
                                                k2=1
                                            
                                            N_5+=Y1
                                        
                                    
                                            circuit.cp(N_5, k1, k2)
                                            
                                            
                                            Times_11+=Y1
                                            circuit.cp(Times_11,k1,k2)
                                            
                                                                              
                                           
                                            if N_5==(2**24)-1:
                                            
                                                
                                                Times_10+=1
                                                circuit.cp(Times_10,k1,k2)
                                                
                                         
                                                N_5=0
                                            if Times_10==(2**24)-1:
                                         
                                                
                                                Times_10=1
                                            if Times_11==(2**32)-1:
                                                
                                                
                                                Times_7+=1
                                                circuit.cp(Times_7,k1,k2)
                                    
                                               
                                                Times_11=0
                                             
                                            
                                             
                                                                                    
                                            
                                            
                                           
                            
                                            Times_8=Times_7
                                            Times_9=bin(Times_7)[2:]
                                            long_T=len(Times_9)
                                            long_T=(long_T//8)+1
                                            Combinate=""
                                            Combinate="0"+str(long_T*8)+"b"
                                            
 
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file2=""
                                            Equal_info_between_of_the_cirlce_of_the_file3=""
                                            Equal_info_between_of_the_cirlce_of_the_file4=""
                                            Add_N=""
    
                                           
                                            Equal_info_between_of_the_cirlce_of_the_file2=format(N_5,'024b')
                                            Equal_info_between_of_the_cirlce_of_the_file3=format(Times_10,'024b')
                                            
                                            

                                            Add_N=format(Times_11,'032b')

                                            
                                            Equal_info_between_of_the_cirlce_of_the_file4=format(Times_8,Combinate)
                                           
                                             
                                            
                                            Info=Equal_info_between_of_the_cirlce_of_the_file4
                                            
                                            
                                            
                                                
                                            
                                            #print(B)
                                               
                                           
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file3=format(Times_10,'016b')                                            
                                            
                                                                                   
                                            
                                                                                         
                                                
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file4
    
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=""
                                      
                                            
                                            
                                            lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
    
    
                                            add_bits=""
    
                                            Times_6=""
    
                                            #Extract
    
                                            sda10=""
                                            Translate_info_Decimal=""
                                          
                                           
                                            Times_6=""
                                        
                                            Number_of_the_file=0
                                          
    
                                            C=1
                                         
                                            if C==1:
                                                if   Circle_times2==0:
    
                                                         
    
                                                        
    
                                                        
                                                        
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
    
                                                        sda10=Equal_info_between_of_the_cirlce_of_the_file2
                                                        Deep5 = int(sda10, 2)
                                                       
                                                      
                                                        
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file_2
                                                        
                                                      
                                                        
                                                        Times_6=Equal_info_between_of_the_cirlce_of_the_file3
                                                        Add_N=Add_N
                                                        
                                                        T = int(Times_6, 2)
                                                        Add= int(Add_N, 2)
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                        #print("Deep: ")
                                                        #print(Deep7-25)
                                                        Times_half_Real=0
                                                if   Circle_times2>0:
                                                        Translate_info_Decimal_2=0
                                                        
                                                
                                                        
            
                                                if C==1 and T!=0:
                                                        Equal_info_between_of_the_cirlce_of_the_file4=Equal_info_between_of_the_cirlce_of_the_file4
                                                        lenf6=len(Equal_info_between_of_the_cirlce_of_the_file4)
                                                       
                                                        
                                                       
                                                        if len (Equal_info_between_of_the_cirlce_of_the_file4)!=0:
                        
                                                                                                    
                                                            Number_of_the_file=int(Equal_info_between_of_the_cirlce_of_the_file4, 2)
                                                                                                     

                                                        else:
                                                            Number_of_the_file=0
                                          
                                                        Hole_Number_information=(2**Deep5)-1
                                                        add_ones_together=Hole_Number_information
                                                
                                                
                                                                                          
                                                        Number_of_the_file=int(((Number_of_the_file*add_ones_together)+Add)//3)
                                                        if Number_of_the_file==1:
                                                            Y1=40
                                                        if int(sda,2)<=Number_of_the_file+80:
                                                            Y1=1
                                                        if int(sda,2)<=Number_of_the_file-1:
                                                            Times_10=0
                                                        
                                                        Times_half_Real+=1
                                                        
                                                        
                                                        
                                                
                                        
                                                
                                                                                  
                                                
                                                
                                                        
                                               

                                              
                                            #####################################################################################################################################################
                                           
                                            
                                            
                                            
                                            Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                             
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                            #print(Equal_info_between_of_the_cirlce_of_the_file_17)
                                           
    
                                            if i==1:
                                                Make_togher=""
                                                Make_togher=Times_6
                                                
                                                add_bits=""
                                                if C==1 and T!=0:
                                                        Circle_times2=Circle_times2+1
    
                                                lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                #print(Circle_times2)
                                                
                                                
                                                if  Circle_times2==T:
                                                        Circle_times2=0
                                                        
                                                        if int(sda,2)<=Number_of_the_file:  
                                                               if C==1 and T==0:
                                                                       Equal_info_between_of_the_cirlce_of_the_file_17=sda
                                                                       lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                       add_bits=""
                                                                       count_bits=8-lenf%8
                                                                       z=0
                                                                       if count_bits!=0:
                                                                               if count_bits!=8:
                                                                                   while z<count_bits:
                                                                                       add_bits="0"+add_bits
                                                                                       z=z+1
                                                                       Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                                               if C==1 and T!=0:

                                                                       Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                                                       lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)



                                                                       lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                                       add_bits=""
                                                                       count_bits=8-lenf%8
                                                                       z=0
                                                                       if count_bits!=0:
                                                                               if count_bits!=8:
                                                                                   while z<count_bits:
                                                                                       add_bits="0"+add_bits
                                                                                       z=z+1


                                                                       Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                                #print(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                if int(sda,2)<=Number_of_the_file:   
                                                       lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                       add_bits=""
                                                       count_bits=8-lenf%8
                                                       z=0
                                                       if count_bits!=0:
                                                               if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1
                                                       Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17        








                                                       Time_Real=bin(lenf2)[2:]
                                                       T1=len(Time_Real)
                                                       T2=(T1//8)+1
                                                       T2=T2*8

                                                       C="0"+str(T2)+"b"
                                                       Time_Real3=format(lenf2,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=format(T1,'08b')
                                                       long3=Time_Real1+Time_Real3




                                                       Time_Real=bin(Times_11)[2:]
                                                       T1=len(Time_Real)
                                                       T2=(T1//8)+1
                                                       T2=T2*8

                                                       C="0"+str(T2)+"b"
                                                       Time_Real3=format(Times_11,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=format(T1,'08b')
                                                       Add_N=Time_Real1+Time_Real3





                                                       Time_Real=bin(T)[2:]
                                                       T1=len(Time_Real)
                                                       T2=(T1//8)+1
                                                       T2=T2*8

                                                       C="0"+str(T2)+"b"
                                                       Time_Real3=format(T,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=format(T1,'016b')
                                                       Time_Real2=Time_Real1+Time_Real3





                                                       Time_Real=bin(N_5)[2:]
                                                       T1=len(Time_Real)
                                                       T2=(T1//8)+1
                                                       T2=T2*8

                                                       C="0"+str(T2)+"b"
                                                       Time_Real3=format(N_5,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=format(T1,'08b')
                                                       Equal_info_between_of_the_cirlce_of_the_file2=Time_Real1+Time_Real3






                                                       Time_Real=bin(Times_10)[2:]
                                                       T1=len(Time_Real)
                                                       T2=(T1//8)+1
                                                       T2=T2*8

                                                       C="0"+str(T2)+"b"
                                                       Time_Real3=format(Times_10,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=format(T1,'08b')
                                                       Equal_info_between_of_the_cirlce_of_the_file3=Time_Real1+Time_Real3





                                                       Time_Real=bin(Times_half_Real)[2:]
                                                       T1=len(Time_Real)
                                                       T2=(T1//8)+1
                                                       T2=T2*8

                                                       C="0"+str(T2)+"b"
                                                       Time_Real3=format(Times_half_Real,C)
                                                       T1=len(Time_Real3)
                                                       Time_Real1=format(T1,'016b')
                                                       Reality=Time_Real1+Time_Real3
                                                       #print(T)





                                                       if Extact==Equal_info_between_of_the_cirlce_of_the_file_17 and T!=0:


                                                               Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file2+Equal_info_between_of_the_cirlce_of_the_file3+Add_N+long3+Time_Real2+Reality+Info
                                                               Extract1=1

                                                       if Extact==Equal_info_between_of_the_cirlce_of_the_file_17 and T==0:
                                                               Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file2+Equal_info_between_of_the_cirlce_of_the_file3+Add_N+long3+Time_Real2+Reality+sda
                                                               Extract1=1  
                                                       if int(sda,2)==0:
                                                               Equal_info_between_of_the_cirlce_of_the_file_17=Compress_zeros
                                                               lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                               add_bits=""
                                                               count_bits=8-lenf%8
                                                               z=0
                                                               if count_bits!=0:
                                                                   if count_bits!=8:
                                                                       while z<count_bits:
                                                                               add_bits="0"+add_bits
                                                                               z=z+1

                                                               Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                                               Extract1=1
                                                    
                                                        
                                    if Extract1==1:                
                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)
                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                            
                                  
                                                            
                                            with open(nameas, "wb") as f2:
                                                f2.write(width_bits3)
                                                    
                                            
                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
                                    		
                                if i==2:
                                   
                                    Equal_info_between_of_the_cirlce_of_the_file_17=""
                                    lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                    if  len(sda)<=(14*8):
                                                 
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_17
                                                    #print(Number_zeroes)
                                                    Number_zeroes=int(sda,2)
                                                    Number_zeroes-=1
                                                    Equal_info_between_of_the_cirlce_of_the_file_18=""
                                                   
                                                    Number_zeroes1=0
                                                    while Number_zeroes!=Number_zeroes1:
                                                            Equal_info_between_of_the_cirlce_of_the_file_18=Equal_info_between_of_the_cirlce_of_the_file_18+"0"
                                                            Number_zeroes1+=1
                                                    Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file_18

                                                    lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                                    add_bits=""
                                                    count_bits=8-lenf%8
                                                    z=0
                                                    if count_bits!=0:
                                                            if count_bits!=8:
                                                                    while z<count_bits:
                                                                            add_bits="0"+add_bits
                                                                            z=z+1

                                                    Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                                    L=len(Equal_info_between_of_the_cirlce_of_the_file_17)

                                                    n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)

                                                    width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)

                                                    width_bits=(width_bits//8)*2

                                                    width_bits=str(width_bits)
                                                    width_bits="%0"+width_bits+"x"
                                                    width_bits3=binascii.unhexlify(width_bits % n)
                                                    width_bits2=len(width_bits3)
                                                    add_bitszzza=""
                                                    add_bitszs=""
                                                    Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                                    with open(nameas, "wb") as f2:
                                                            f2.write(width_bits3)
                                                    x2 = time()
                                                    x3=x2-x
                                                    xs=float(x3)
                                                    return print(x3)
                                   

                                    
                                   
                   
                               
                                            
                                            
                                              

                                            
                                           
                                            
                           
                       
                                                            
                                              
                              
                                    Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file_2
                                   
                                    
                                   
                                    
                                    
                                    
                                    lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                    add_bits=""

                                    Times_6=""

                                    #Extract

                                    sda10=""
                                    Translate_info_Decimal=""
                                  
                                    Number_add_plus_one=""
                                  
                                    Times_6=""
                                
                                    Number_of_the_file=0
                                    
                                 

                                    
                                 
                                    if C==1:
                                        
                                        if   Circle_times2==0:
                                            Equal_info_between_of_the_cirlce_of_the_file=sda
                                           
                                        if   Circle_times2==0:
                                
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:8],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                Deep5=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                               
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:8],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                T=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]

                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:8],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                Add=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:8],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[8:]
                                                long=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                
                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:16],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[16:]
                                                T_Real=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                              
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]

                                                Real_C=int(Equal_info_between_of_the_cirlce_of_the_file[0:16],2)
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[16:]
                                                Reality=int(Equal_info_between_of_the_cirlce_of_the_file[:Real_C],2)
                                                #print(Reality)
                                              
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file[Real_C:]
                                                
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)

                                                #print(Reality)
                                                Reality2=0
                                                
                                        if   Circle_times2>0:
                                        	Translate_info_Decimal_2=0
                                        	
                                        
                                        	
    
                                        if C==1 and T!=0:
                                                Equal_info_between_of_the_cirlce_of_the_file=Equal_info_between_of_the_cirlce_of_the_file
                                                lenf6=len(Equal_info_between_of_the_cirlce_of_the_file)
                                                


                                                if len (Equal_info_between_of_the_cirlce_of_the_file)!=0:
                        
                                                                                                    
                                                    Number_of_the_file=int(Equal_info_between_of_the_cirlce_of_the_file,2)

                                                else:
                                                     Number_of_the_file=0
                                                     
                                                if Reality2<Reality:
                                                        Hole_Number_information=(2**Deep5)-1
                                                        add_ones_together=Hole_Number_information
                                                        Reality2+=1
                                                        Number_of_the_file=((Number_of_the_file*add_ones_together)+Add)//3
                                                        #print(Number_of_the_file)
                                             
                                    #####################################################################################################################################################
                                   
                                    
                                    
                                    
                                    Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                     
                                    Equal_info_between_of_the_cirlce_of_the_file_2=Equal_info_between_of_the_cirlce_of_the_file_17
                                   

                                    if i==2:
                                        Make_togher=""
                                        Make_togher=Times_6
                                        Number_add_plus_one=""
                                        add_bits=""
                                        if C==1 and T!=0:
                                                Circle_times2=Circle_times2+1

                                        lenf9=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                        #print(Circle_times2)
                                        
                                        
                                          
                                        
                                                
                                        if  Circle_times2==T_Real:
                                        	   
                                            if C==1 and T==0:
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=Equal_info_between_of_the_cirlce_of_the_file
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=long-lenf%long
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=long:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17


                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            	
                                            
                                     
                                            if C==1 and T!=0:
 
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=bin(Number_of_the_file)[2:]
                                            	lenf14=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=long-lenf%long
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=long:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17

                                            	
                                            	lenf=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            	add_bits=""
                                            	count_bits=8-lenf%8
                                            	z=0
                                            	if count_bits!=0:
                                            	        if count_bits!=8:
                                            	            while z<count_bits:
                                            	            	add_bits="0"+add_bits
                                            	            	z=z+1
                                            	Equal_info_between_of_the_cirlce_of_the_file_17=add_bits+Equal_info_between_of_the_cirlce_of_the_file_17
                                            	        
                                            	#print(lenf14)

                                            		
                                            	
                                            	
                                            L=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                         
                                            n = int(Equal_info_between_of_the_cirlce_of_the_file_17, 2)
                                            width_bits=len(Equal_info_between_of_the_cirlce_of_the_file_17)
                                            width_bits=(width_bits//8)*2
                                            width_bits=str(width_bits)
                                            width_bits="%0"+width_bits+"x"
                                            width_bits3=binascii.unhexlify(width_bits % n)
                                            width_bits2=len(width_bits3)

                                            add_bitszzza=""
                                            add_bitszs=""
                                            Equal_info_between_of_the_cirlce_of_the_file_2=Times_6
                                             
                                            with open(nameas, "wb") as f2:
                                            
                                              
                                            	f2.write(width_bits3)

                                            x2 = time()
                                            x3=x2-x
                                            xs=float(x3)
                                            return print(x3)
   
d=compression()

xw1=d.cryptograpy_compression4()
print(xw1)
