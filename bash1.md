```bash
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=35
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s2) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s15) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s28) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s3) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s7) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s11) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s4) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s5) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s6) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h1) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h2) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h3) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h4) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h5) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h6) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h7) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h8) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h9) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s8) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s9) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s10) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h10) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h11) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h12) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h13) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h14) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h15) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h16) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h17) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h18) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s12) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s13) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s14) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h19) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h20) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h21) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h22) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h23) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h24) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h25) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h26) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h27) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s16) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s20) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s24) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s17) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s18) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s19) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h28) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h29) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h30) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h31) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h32) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h33) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h34) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h35) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h36) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s21) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s22) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s23) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h37) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h38) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h39) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h40) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h41) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h42) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h43) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h44) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h45) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s25) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s26) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s27) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h46) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h47) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h48) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h49) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h50) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h51) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h52) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h53) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h54) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s29) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s33) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s37) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s30) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s31) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s32) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h55) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h56) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h57) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h58) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h59) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h60) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h61) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h62) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h63) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s34) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s35) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s36) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h64) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h65) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h66) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h67) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h68) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h69) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h70) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h71) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h72) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s38) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s39) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s40) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h73) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h74) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h75) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h76) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h77) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h78) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h79) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h80) (35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(35.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.

*** Starting CLI:
mininet> h1 ping h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.10 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.310 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.401 ms
64 bytes from 10.0.0.2: icmp_seq=4 ttl=64 time=0.547 ms
64 bytes from 10.0.0.2: icmp_seq=5 ttl=64 time=0.285 ms
64 bytes from 10.0.0.2: icmp_seq=6 ttl=64 time=0.218 ms
64 bytes from 10.0.0.2: icmp_seq=7 ttl=64 time=0.242 ms
64 bytes from 10.0.0.2: icmp_seq=8 ttl=64 time=0.145 ms
^C
--- 10.0.0.2 ping statistics ---
8 packets transmitted, 8 received, 0% packet loss, time 7023ms
rtt min/avg/max/mdev = 0.145/0.406/1.100/0.286 ms
mininet> h1 ifconfig
h1-eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet 10.0.0.1  netmask 255.0.0.0  broadcast 10.255.255.255
        inet6 fe80::200:ff:fe00:1  prefixlen 64  scopeid 0x20<link>
        ether 00:00:00:00:00:01  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet> h1 ip addr
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
    inet6 ::1/128 scope host
       valid_lft forever preferred_lft forever
2: h1-eth0@if1021: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc htb state UP group default qlen 1000
    link/ether 00:00:00:00:00:01 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.0.0.1/8 brd 10.255.255.255 scope global h1-eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::200:ff:fe00:1/64 scope link
       valid_lft forever preferred_lft forever
mininet> h1 ping -c 1 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.59 ms

--- 10.0.0.2 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 1.588/1.588/1.588/0.000 ms
mininet> h1 arp -n
Address                  HWtype  HWaddress           Flags Mask            Iface
10.0.0.2                 ether   00:00:00:00:00:02   C                     h1-eth0
mininet> s1 ifconfig
eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1382
        inet 172.25.134.146  netmask 255.255.240.0  broadcast 172.25.143.255
        inet6 fe80::215:5dff:fede:560f  prefixlen 64  scopeid 0x20<link>
        ether 00:15:5d:de:56:0f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536
        inet 127.0.0.1  netmask 255.0.0.0
        inet6 ::1  prefixlen 128  scopeid 0x10<host>
        loop  txqueuelen 1000  (Local Loopback)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s1-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::109a:eaff:fe4c:f982  prefixlen 64  scopeid 0x20<link>
        ether 12:9a:ea:4c:f9:82  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s1-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c44d:26ff:feb0:6009  prefixlen 64  scopeid 0x20<link>
        ether c6:4d:26:b0:60:09  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s1-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::a83b:5bff:fe4a:dbee  prefixlen 64  scopeid 0x20<link>
        ether aa:3b:5b:4a:db:ee  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s10-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::fc72:a8ff:fe92:70f2  prefixlen 64  scopeid 0x20<link>
        ether fe:72:a8:92:70:f2  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s10-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::e494:49ff:fe32:595a  prefixlen 64  scopeid 0x20<link>
        ether e6:94:49:32:59:5a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s10-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::14ba:5cff:fe77:169a  prefixlen 64  scopeid 0x20<link>
        ether 16:ba:5c:77:16:9a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s10-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::80a2:2fff:fe35:b499  prefixlen 64  scopeid 0x20<link>
        ether 82:a2:2f:35:b4:99  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s11-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c01a:19ff:fe82:2451  prefixlen 64  scopeid 0x20<link>
        ether c2:1a:19:82:24:51  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s11-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8c4e:90ff:feac:8dab  prefixlen 64  scopeid 0x20<link>
        ether 8e:4e:90:ac:8d:ab  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s11-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::9b:e8ff:fe26:39f6  prefixlen 64  scopeid 0x20<link>
        ether 02:9b:e8:26:39:f6  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s11-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::cca4:2fff:febf:f9b4  prefixlen 64  scopeid 0x20<link>
        ether ce:a4:2f:bf:f9:b4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s12-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::54ad:d3ff:fe4c:1285  prefixlen 64  scopeid 0x20<link>
        ether 56:ad:d3:4c:12:85  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s12-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::84b7:9aff:feaf:a928  prefixlen 64  scopeid 0x20<link>
        ether 86:b7:9a:af:a9:28  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s12-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::bcc7:fdff:fe3a:58bd  prefixlen 64  scopeid 0x20<link>
        ether be:c7:fd:3a:58:bd  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s12-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::bcef:4aff:febd:3a05  prefixlen 64  scopeid 0x20<link>
        ether be:ef:4a:bd:3a:05  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s13-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2864:13ff:fe13:1cc0  prefixlen 64  scopeid 0x20<link>
        ether 2a:64:13:13:1c:c0  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s13-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c832:4aff:fedc:3ae1  prefixlen 64  scopeid 0x20<link>
        ether ca:32:4a:dc:3a:e1  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s13-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d8dc:e6ff:fe8b:8032  prefixlen 64  scopeid 0x20<link>
        ether da:dc:e6:8b:80:32  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s13-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c410:dff:fe45:f3b9  prefixlen 64  scopeid 0x20<link>
        ether c6:10:0d:45:f3:b9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s14-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::fc26:f2ff:fe3e:b82f  prefixlen 64  scopeid 0x20<link>
        ether fe:26:f2:3e:b8:2f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s14-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7828:78ff:fe0c:2483  prefixlen 64  scopeid 0x20<link>
        ether 7a:28:78:0c:24:83  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s14-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2435:1eff:fe8a:8b7d  prefixlen 64  scopeid 0x20<link>
        ether 26:35:1e:8a:8b:7d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s14-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8c17:fcff:feb9:b9ea  prefixlen 64  scopeid 0x20<link>
        ether 8e:17:fc:b9:b9:ea  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s15-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::845a:70ff:fef3:b1a  prefixlen 64  scopeid 0x20<link>
        ether 86:5a:70:f3:0b:1a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s15-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::5c97:48ff:fe38:c016  prefixlen 64  scopeid 0x20<link>
        ether 5e:97:48:38:c0:16  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s15-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::38a6:2dff:fe61:abb  prefixlen 64  scopeid 0x20<link>
        ether 3a:a6:2d:61:0a:bb  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s15-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::5c7a:2fff:fe20:8272  prefixlen 64  scopeid 0x20<link>
        ether 5e:7a:2f:20:82:72  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s16-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d4ed:29ff:fed3:bde  prefixlen 64  scopeid 0x20<link>
        ether d6:ed:29:d3:0b:de  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s16-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::64a3:6fff:fef0:614d  prefixlen 64  scopeid 0x20<link>
        ether 66:a3:6f:f0:61:4d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s16-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::cce0:9aff:feb5:2d73  prefixlen 64  scopeid 0x20<link>
        ether ce:e0:9a:b5:2d:73  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s16-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7456:c6ff:fefd:d4dd  prefixlen 64  scopeid 0x20<link>
        ether 76:56:c6:fd:d4:dd  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s17-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::a8d5:ff:fedb:85d9  prefixlen 64  scopeid 0x20<link>
        ether aa:d5:00:db:85:d9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s17-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::70d4:f0ff:fe61:78ab  prefixlen 64  scopeid 0x20<link>
        ether 72:d4:f0:61:78:ab  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s17-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f00e:64ff:fea2:488f  prefixlen 64  scopeid 0x20<link>
        ether f2:0e:64:a2:48:8f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s17-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::e8af:dfff:fe11:a393  prefixlen 64  scopeid 0x20<link>
        ether ea:af:df:11:a3:93  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s18-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c8e0:ff:fe9a:a4f4  prefixlen 64  scopeid 0x20<link>
        ether ca:e0:00:9a:a4:f4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s18-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::482f:ecff:febd:a5f8  prefixlen 64  scopeid 0x20<link>
        ether 4a:2f:ec:bd:a5:f8  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s18-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d807:b5ff:fec4:1d69  prefixlen 64  scopeid 0x20<link>
        ether da:07:b5:c4:1d:69  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s18-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c870:29ff:fe35:3fc5  prefixlen 64  scopeid 0x20<link>
        ether ca:70:29:35:3f:c5  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s19-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ecb4:94ff:fedd:275  prefixlen 64  scopeid 0x20<link>
        ether ee:b4:94:dd:02:75  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s19-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f8b6:9fff:fe5a:fa42  prefixlen 64  scopeid 0x20<link>
        ether fa:b6:9f:5a:fa:42  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s19-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6c76:80ff:fe88:8f2f  prefixlen 64  scopeid 0x20<link>
        ether 6e:76:80:88:8f:2f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s19-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f08a:c6ff:fef9:598  prefixlen 64  scopeid 0x20<link>
        ether f2:8a:c6:f9:05:98  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c07d:28ff:fe42:b0bc  prefixlen 64  scopeid 0x20<link>
        ether c2:7d:28:42:b0:bc  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::1:89ff:fe06:726d  prefixlen 64  scopeid 0x20<link>
        ether 02:01:89:06:72:6d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4c72:5bff:fe6d:79ff  prefixlen 64  scopeid 0x20<link>
        ether 4e:72:5b:6d:79:ff  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s2-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::5cc3:5aff:fece:398c  prefixlen 64  scopeid 0x20<link>
        ether 5e:c3:5a:ce:39:8c  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s20-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::401e:90ff:fe60:efe6  prefixlen 64  scopeid 0x20<link>
        ether 42:1e:90:60:ef:e6  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s20-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6433:b7ff:fef5:9cc3  prefixlen 64  scopeid 0x20<link>
        ether 66:33:b7:f5:9c:c3  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s20-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6ce5:46ff:fe79:15ba  prefixlen 64  scopeid 0x20<link>
        ether 6e:e5:46:79:15:ba  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s20-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::5c97:fcff:fe7d:c533  prefixlen 64  scopeid 0x20<link>
        ether 5e:97:fc:7d:c5:33  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s21-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::490:55ff:fe13:39b4  prefixlen 64  scopeid 0x20<link>
        ether 06:90:55:13:39:b4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s21-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::fc0a:3aff:fe21:50f3  prefixlen 64  scopeid 0x20<link>
        ether fe:0a:3a:21:50:f3  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s21-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::240b:70ff:fe93:be57  prefixlen 64  scopeid 0x20<link>
        ether 26:0b:70:93:be:57  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s21-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::14f2:5cff:fe97:66e3  prefixlen 64  scopeid 0x20<link>
        ether 16:f2:5c:97:66:e3  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s22-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7c5d:12ff:fee0:4016  prefixlen 64  scopeid 0x20<link>
        ether 7e:5d:12:e0:40:16  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s22-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::70e5:59ff:fe6d:c906  prefixlen 64  scopeid 0x20<link>
        ether 72:e5:59:6d:c9:06  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s22-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::608f:e2ff:fe88:6b5a  prefixlen 64  scopeid 0x20<link>
        ether 62:8f:e2:88:6b:5a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s22-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d8f6:a7ff:fef3:46a  prefixlen 64  scopeid 0x20<link>
        ether da:f6:a7:f3:04:6a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s23-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::b4b6:66ff:fee4:8271  prefixlen 64  scopeid 0x20<link>
        ether b6:b6:66:e4:82:71  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s23-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7cff:26ff:feb1:d592  prefixlen 64  scopeid 0x20<link>
        ether 7e:ff:26:b1:d5:92  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s23-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7081:86ff:fe2f:bb83  prefixlen 64  scopeid 0x20<link>
        ether 72:81:86:2f:bb:83  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s23-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6c54:15ff:fe59:5735  prefixlen 64  scopeid 0x20<link>
        ether 6e:54:15:59:57:35  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s24-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::bc62:12ff:fea0:40d8  prefixlen 64  scopeid 0x20<link>
        ether be:62:12:a0:40:d8  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s24-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::80b8:baff:fec0:2837  prefixlen 64  scopeid 0x20<link>
        ether 82:b8:ba:c0:28:37  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s24-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f861:38ff:fecb:3cdb  prefixlen 64  scopeid 0x20<link>
        ether fa:61:38:cb:3c:db  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s24-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8c52:e9ff:fecb:583e  prefixlen 64  scopeid 0x20<link>
        ether 8e:52:e9:cb:58:3e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s25-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c8f6:abff:fe79:83aa  prefixlen 64  scopeid 0x20<link>
        ether ca:f6:ab:79:83:aa  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s25-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6463:6bff:feca:b82  prefixlen 64  scopeid 0x20<link>
        ether 66:63:6b:ca:0b:82  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s25-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::487f:32ff:fe03:a861  prefixlen 64  scopeid 0x20<link>
        ether 4a:7f:32:03:a8:61  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s25-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8ce7:f0ff:fe8f:c79f  prefixlen 64  scopeid 0x20<link>
        ether 8e:e7:f0:8f:c7:9f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s26-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::1406:d0ff:fe45:744c  prefixlen 64  scopeid 0x20<link>
        ether 16:06:d0:45:74:4c  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s26-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7ccf:b7ff:fe1a:6882  prefixlen 64  scopeid 0x20<link>
        ether 7e:cf:b7:1a:68:82  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s26-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::9886:efff:fee8:29b0  prefixlen 64  scopeid 0x20<link>
        ether 9a:86:ef:e8:29:b0  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s26-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::a405:2ff:fe71:f6ce  prefixlen 64  scopeid 0x20<link>
        ether a6:05:02:71:f6:ce  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s27-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f44f:eaff:fe16:1140  prefixlen 64  scopeid 0x20<link>
        ether f6:4f:ea:16:11:40  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s27-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::88d6:d5ff:fe96:998  prefixlen 64  scopeid 0x20<link>
        ether 8a:d6:d5:96:09:98  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s27-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4c74:89ff:fe2c:c8de  prefixlen 64  scopeid 0x20<link>
        ether 4e:74:89:2c:c8:de  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s27-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::3091:d0ff:feda:adae  prefixlen 64  scopeid 0x20<link>
        ether 32:91:d0:da:ad:ae  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s28-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::74ee:84ff:fea4:ced9  prefixlen 64  scopeid 0x20<link>
        ether 76:ee:84:a4:ce:d9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s28-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::647b:9cff:fe9e:9382  prefixlen 64  scopeid 0x20<link>
        ether 66:7b:9c:9e:93:82  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s28-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4ca8:92ff:febf:2758  prefixlen 64  scopeid 0x20<link>
        ether 4e:a8:92:bf:27:58  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s28-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::9c0d:e5ff:fe6b:5a19  prefixlen 64  scopeid 0x20<link>
        ether 9e:0d:e5:6b:5a:19  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s29-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::a05d:e0ff:fe7c:5689  prefixlen 64  scopeid 0x20<link>
        ether a2:5d:e0:7c:56:89  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s29-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d8c8:faff:feb1:72e6  prefixlen 64  scopeid 0x20<link>
        ether da:c8:fa:b1:72:e6  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s29-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c8ff:e0ff:fedd:d676  prefixlen 64  scopeid 0x20<link>
        ether ca:ff:e0:dd:d6:76  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s29-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d1:ffff:fe97:f4f9  prefixlen 64  scopeid 0x20<link>
        ether 02:d1:ff:97:f4:f9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::685f:2fff:fe9d:965e  prefixlen 64  scopeid 0x20<link>
        ether 6a:5f:2f:9d:96:5e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2c08:59ff:fede:8084  prefixlen 64  scopeid 0x20<link>
        ether 2e:08:59:de:80:84  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::9062:bbff:feb8:6206  prefixlen 64  scopeid 0x20<link>
        ether 92:62:bb:b8:62:06  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s3-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::447:deff:fe7a:1106  prefixlen 64  scopeid 0x20<link>
        ether 06:47:de:7a:11:06  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s30-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::1cc2:c8ff:fed9:e7e6  prefixlen 64  scopeid 0x20<link>
        ether 1e:c2:c8:d9:e7:e6  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s30-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::1ce6:82ff:fe54:763a  prefixlen 64  scopeid 0x20<link>
        ether 1e:e6:82:54:76:3a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s30-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::20d5:90ff:fe01:ac37  prefixlen 64  scopeid 0x20<link>
        ether 22:d5:90:01:ac:37  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s30-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6cc5:75ff:fe6d:13ca  prefixlen 64  scopeid 0x20<link>
        ether 6e:c5:75:6d:13:ca  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s31-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::30a1:36ff:fe52:1eae  prefixlen 64  scopeid 0x20<link>
        ether 32:a1:36:52:1e:ae  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s31-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::489:eff:fe1c:6a9c  prefixlen 64  scopeid 0x20<link>
        ether 06:89:0e:1c:6a:9c  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s31-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::502f:bbff:fef0:c23e  prefixlen 64  scopeid 0x20<link>
        ether 52:2f:bb:f0:c2:3e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s31-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::145f:ecff:fec0:6f6f  prefixlen 64  scopeid 0x20<link>
        ether 16:5f:ec:c0:6f:6f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s32-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::c11:70ff:fe72:e591  prefixlen 64  scopeid 0x20<link>
        ether 0e:11:70:72:e5:91  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s32-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f0ce:dcff:fe1e:e1f4  prefixlen 64  scopeid 0x20<link>
        ether f2:ce:dc:1e:e1:f4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s32-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::105f:75ff:fe43:9a09  prefixlen 64  scopeid 0x20<link>
        ether 12:5f:75:43:9a:09  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s32-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d4ee:aaff:fe95:69ee  prefixlen 64  scopeid 0x20<link>
        ether d6:ee:aa:95:69:ee  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s33-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::a831:59ff:fe7c:63b3  prefixlen 64  scopeid 0x20<link>
        ether aa:31:59:7c:63:b3  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s33-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::3c28:72ff:fe83:19d9  prefixlen 64  scopeid 0x20<link>
        ether 3e:28:72:83:19:d9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s33-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::3045:cfff:fef1:874d  prefixlen 64  scopeid 0x20<link>
        ether 32:45:cf:f1:87:4d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s33-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2406:4dff:fef7:9112  prefixlen 64  scopeid 0x20<link>
        ether 26:06:4d:f7:91:12  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s34-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::905e:b0ff:fe48:ae44  prefixlen 64  scopeid 0x20<link>
        ether 92:5e:b0:48:ae:44  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s34-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::bc16:aeff:fea9:c856  prefixlen 64  scopeid 0x20<link>
        ether be:16:ae:a9:c8:56  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s34-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::38a5:dcff:fec3:7cb  prefixlen 64  scopeid 0x20<link>
        ether 3a:a5:dc:c3:07:cb  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s34-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::1cf8:5aff:fe08:399d  prefixlen 64  scopeid 0x20<link>
        ether 1e:f8:5a:08:39:9d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s35-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6c24:cff:fe61:1e1f  prefixlen 64  scopeid 0x20<link>
        ether 6e:24:0c:61:1e:1f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s35-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ec3c:77ff:fe9c:48a5  prefixlen 64  scopeid 0x20<link>
        ether ee:3c:77:9c:48:a5  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s35-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d8c6:f2ff:fe60:31bd  prefixlen 64  scopeid 0x20<link>
        ether da:c6:f2:60:31:bd  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s35-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7c1a:a8ff:fe20:b572  prefixlen 64  scopeid 0x20<link>
        ether 7e:1a:a8:20:b5:72  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s36-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::28ad:a2ff:fe1e:5066  prefixlen 64  scopeid 0x20<link>
        ether 2a:ad:a2:1e:50:66  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s36-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4852:7eff:fe55:90d4  prefixlen 64  scopeid 0x20<link>
        ether 4a:52:7e:55:90:d4  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s36-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::648c:81ff:fe65:a72c  prefixlen 64  scopeid 0x20<link>
        ether 66:8c:81:65:a7:2c  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s36-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d4c5:5fff:fe86:3851  prefixlen 64  scopeid 0x20<link>
        ether d6:c5:5f:86:38:51  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s37-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::50fd:94ff:fe20:bcef  prefixlen 64  scopeid 0x20<link>
        ether 52:fd:94:20:bc:ef  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s37-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::409e:b1ff:fe08:1921  prefixlen 64  scopeid 0x20<link>
        ether 42:9e:b1:08:19:21  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s37-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::fc16:26ff:fe59:8c36  prefixlen 64  scopeid 0x20<link>
        ether fe:16:26:59:8c:36  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s37-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f49a:daff:fee0:de68  prefixlen 64  scopeid 0x20<link>
        ether f6:9a:da:e0:de:68  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s38-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2c82:3ff:fee0:8244  prefixlen 64  scopeid 0x20<link>
        ether 2e:82:03:e0:82:44  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s38-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::18e0:15ff:fead:a423  prefixlen 64  scopeid 0x20<link>
        ether 1a:e0:15:ad:a4:23  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s38-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::849a:47ff:fee5:8fd9  prefixlen 64  scopeid 0x20<link>
        ether 86:9a:47:e5:8f:d9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s38-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ac3d:e1ff:fefc:e82e  prefixlen 64  scopeid 0x20<link>
        ether ae:3d:e1:fc:e8:2e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s39-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::1cb3:6fff:fe7d:3699  prefixlen 64  scopeid 0x20<link>
        ether 1e:b3:6f:7d:36:99  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s39-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f88e:5fff:fead:d0f5  prefixlen 64  scopeid 0x20<link>
        ether fa:8e:5f:ad:d0:f5  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s39-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2416:d5ff:febe:bd39  prefixlen 64  scopeid 0x20<link>
        ether 26:16:d5:be:bd:39  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s39-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::b0c5:e2ff:fe4a:664a  prefixlen 64  scopeid 0x20<link>
        ether b2:c5:e2:4a:66:4a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4ae:a2ff:fe4a:396e  prefixlen 64  scopeid 0x20<link>
        ether 06:ae:a2:4a:39:6e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7801:7dff:fea9:e47e  prefixlen 64  scopeid 0x20<link>
        ether 7a:01:7d:a9:e4:7e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::e0b0:55ff:fe2e:9c9  prefixlen 64  scopeid 0x20<link>
        ether e2:b0:55:2e:09:c9  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s4-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::d4c4:13ff:fe11:a4c3  prefixlen 64  scopeid 0x20<link>
        ether d6:c4:13:11:a4:c3  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s40-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4840:4eff:fead:cb81  prefixlen 64  scopeid 0x20<link>
        ether 4a:40:4e:ad:cb:81  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s40-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::90ed:2aff:fe71:7888  prefixlen 64  scopeid 0x20<link>
        ether 92:ed:2a:71:78:88  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s40-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::147f:ecff:fe21:7c6d  prefixlen 64  scopeid 0x20<link>
        ether 16:7f:ec:21:7c:6d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s40-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f015:60ff:fed7:7d56  prefixlen 64  scopeid 0x20<link>
        ether f2:15:60:d7:7d:56  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::6cc6:cfff:fe2b:658f  prefixlen 64  scopeid 0x20<link>
        ether 6e:c6:cf:2b:65:8f  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2c40:a5ff:fe46:dfec  prefixlen 64  scopeid 0x20<link>
        ether 2e:40:a5:46:df:ec  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::e476:e1ff:fe48:8bbc  prefixlen 64  scopeid 0x20<link>
        ether e6:76:e1:48:8b:bc  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s5-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::dc19:b7ff:fe86:44ee  prefixlen 64  scopeid 0x20<link>
        ether de:19:b7:86:44:ee  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s6-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::dca2:3cff:fe14:6eea  prefixlen 64  scopeid 0x20<link>
        ether de:a2:3c:14:6e:ea  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s6-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::80d0:b8ff:fef0:5c9a  prefixlen 64  scopeid 0x20<link>
        ether 82:d0:b8:f0:5c:9a  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s6-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::34b7:baff:fe8e:9a47  prefixlen 64  scopeid 0x20<link>
        ether 36:b7:ba:8e:9a:47  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s6-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::4c33:bdff:fe47:119d  prefixlen 64  scopeid 0x20<link>
        ether 4e:33:bd:47:11:9d  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s7-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::642e:a3ff:fe7d:8665  prefixlen 64  scopeid 0x20<link>
        ether 66:2e:a3:7d:86:65  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s7-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::8040:a4ff:fe71:ed85  prefixlen 64  scopeid 0x20<link>
        ether 82:40:a4:71:ed:85  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s7-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::ec78:21ff:fe52:4f2  prefixlen 64  scopeid 0x20<link>
        ether ee:78:21:52:04:f2  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s7-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::2872:8cff:feda:9559  prefixlen 64  scopeid 0x20<link>
        ether 2a:72:8c:da:95:59  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s8-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::f419:b0ff:fedb:bdc7  prefixlen 64  scopeid 0x20<link>
        ether f6:19:b0:db:bd:c7  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s8-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::bc23:a0ff:fe18:22b1  prefixlen 64  scopeid 0x20<link>
        ether be:23:a0:18:22:b1  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s8-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::9421:15ff:feea:d516  prefixlen 64  scopeid 0x20<link>
        ether 96:21:15:ea:d5:16  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s8-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::340b:87ff:fe80:ebd3  prefixlen 64  scopeid 0x20<link>
        ether 36:0b:87:80:eb:d3  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s9-eth1: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::7434:6aff:fe44:58c1  prefixlen 64  scopeid 0x20<link>
        ether 76:34:6a:44:58:c1  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s9-eth2: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::38f3:d2ff:feed:efad  prefixlen 64  scopeid 0x20<link>
        ether 3a:f3:d2:ed:ef:ad  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s9-eth3: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::3c17:f0ff:fe24:4a4e  prefixlen 64  scopeid 0x20<link>
        ether 3e:17:f0:24:4a:4e  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

s9-eth4: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500
        inet6 fe80::18e1:1eff:fe2c:5d77  prefixlen 64  scopeid 0x20<link>
        ether 1a:e1:1e:2c:5d:77  txqueuelen 1000  (Ethernet)
        RX packets 0  bytes 0 (0.0 B)
        RX errors 0  dropped 0  overruns 0  frame 0
        TX packets 0  bytes 0 (0.0 B)
        TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

mininet> h2 tcpdump -i h2-eth0 -n icmp &
mininet> h1 ping -c 3 h2
PING 10.0.0.2 (10.0.0.2) 56(84) bytes of data.
64 bytes from 10.0.0.2: icmp_seq=1 ttl=64 time=1.63 ms
64 bytes from 10.0.0.2: icmp_seq=2 ttl=64 time=0.404 ms
64 bytes from 10.0.0.2: icmp_seq=3 ttl=64 time=0.291 ms

--- 10.0.0.2 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2005ms
rtt min/avg/max/mdev = 0.291/0.776/1.634/0.608 ms
mininet> h2 jobs
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on h2-eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:24:02.715764 IP 10.0.0.1 > 10.0.0.2: ICMP echo request, id 11715, seq 1, length 64
14:24:02.715871 IP 10.0.0.2 > 10.0.0.1: ICMP echo reply, id 11715, seq 1, length 64
14:24:03.717095 IP 10.0.0.1 > 10.0.0.2: ICMP echo request, id 11715, seq 2, length 64
14:24:03.717178 IP 10.0.0.2 > 10.0.0.1: ICMP echo reply, id 11715, seq 2, length 64
14:24:04.719299 IP 10.0.0.1 > 10.0.0.2: ICMP echo request, id 11715, seq 3, length 64
14:24:04.719380 IP 10.0.0.2 > 10.0.0.1: ICMP echo reply, id 11715, seq 3, length 64
[1]+  Running                 tcpdump -i h2-eth0 -n icmp &
mininet> h2 kill %1

6 packets captured
6 packets received by filter
0 packets dropped by kernel
mininet> h4 tcpdump -i h4-eth0 -n icmp &
mininet> h1 ping -c 3 h4
PING 10.0.0.4 (10.0.0.4) 56(84) bytes of data.
64 bytes from 10.0.0.4: icmp_seq=1 ttl=64 time=5.56 ms
64 bytes from 10.0.0.4: icmp_seq=2 ttl=64 time=1.91 ms
64 bytes from 10.0.0.4: icmp_seq=3 ttl=64 time=1.07 ms

--- 10.0.0.4 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 1.071/2.846/5.562/1.950 ms
mininet> h4 jobs
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on h4-eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:25:49.482237 IP 10.0.0.1 > 10.0.0.4: ICMP echo request, id 11726, seq 1, length 64
14:25:49.482621 IP 10.0.0.4 > 10.0.0.1: ICMP echo reply, id 11726, seq 1, length 64
14:25:50.480728 IP 10.0.0.1 > 10.0.0.4: ICMP echo request, id 11726, seq 2, length 64
14:25:50.481014 IP 10.0.0.4 > 10.0.0.1: ICMP echo reply, id 11726, seq 2, length 64
14:25:51.482133 IP 10.0.0.1 > 10.0.0.4: ICMP echo request, id 11726, seq 3, length 64
14:25:51.482281 IP 10.0.0.4 > 10.0.0.1: ICMP echo reply, id 11726, seq 3, length 64
[1]+  Running                 tcpdump -i h4-eth0 -n icmp &
mininet> h4 kill %1

6 packets captured
6 packets received by filter
0 packets dropped by kernel
mininet> h81 tcpdump -i h81-eth0 -n icmp &
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
64 bytes from 10.0.0.81: icmp_seq=1 ttl=64 time=8.97 ms
64 bytes from 10.0.0.81: icmp_seq=2 ttl=64 time=0.866 ms
64 bytes from 10.0.0.81: icmp_seq=3 ttl=64 time=1.21 ms

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2003ms
rtt min/avg/max/mdev = 0.866/3.682/8.972/3.743 ms
mininet> h81 jobs
tcpdump: verbose output suppressed, use -v[v]... for full protocol decode
listening on h81-eth0, link-type EN10MB (Ethernet), snapshot length 262144 bytes
14:26:38.002600 IP 10.0.0.1 > 10.0.0.81: ICMP echo request, id 11735, seq 1, length 64
14:26:38.002726 IP 10.0.0.81 > 10.0.0.1: ICMP echo reply, id 11735, seq 1, length 64
14:26:38.997281 IP 10.0.0.1 > 10.0.0.81: ICMP echo request, id 11735, seq 2, length 64
14:26:38.997387 IP 10.0.0.81 > 10.0.0.1: ICMP echo reply, id 11735, seq 2, length 64
14:26:39.999093 IP 10.0.0.1 > 10.0.0.81: ICMP echo request, id 11735, seq 3, length 64
14:26:39.999174 IP 10.0.0.81 > 10.0.0.1: ICMP echo reply, id 11735, seq 3, length 64
[1]+  Running                 tcpdump -i h81-eth0 -n icmp &
mininet> h81 kill %1

6 packets captured
6 packets received by filter
0 packets dropped by kernel
mininet> py h1.IP()
10.0.0.1
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 33958 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/1453)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  4.25 MBytes  35.7 Mbits/sec
[  1] 1.0000-2.0000 sec  4.12 MBytes  34.6 Mbits/sec
[  1] 2.0000-3.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 3.0000-4.0000 sec  4.12 MBytes  34.6 Mbits/sec
[  1] 4.0000-5.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 5.0000-6.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 6.0000-7.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 7.0000-8.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 8.0000-9.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 9.0000-10.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 10.0000-11.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 11.0000-12.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 12.0000-13.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 13.0000-14.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 14.0000-15.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 15.0000-16.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 16.0000-17.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 17.0000-18.0000 sec  4.25 MBytes  35.7 Mbits/sec
[  1] 18.0000-19.0000 sec  3.88 MBytes  32.5 Mbits/sec
[  1] 19.0000-20.0000 sec  4.00 MBytes  33.6 Mbits/sec
[  1] 0.0000-20.1657 sec  80.4 MBytes  33.4 Mbits/sec
mininet> exit
*** Stopping 1 controllers
c0
*** Stopping 120 links
........................................................................................................................
*** Stopping 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Stopping 81 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Done
completed in 649.678 seconds
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=25
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s2) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s15) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s1, s28) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s3) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s7) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s2, s11) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s4) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s5) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s3, s6) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h1) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h2) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s4, h3) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h4) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h5) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s5, h6) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h7) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h8) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s6, h9) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s8) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s9) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s7, s10) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h10) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h11) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s8, h12) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h13) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h14) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s9, h15) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h16) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h17) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s10, h18) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s12) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s13) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s11, s14) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h19) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h20) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s12, h21) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h22) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h23) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s13, h24) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h25) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h26) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s14, h27) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s16) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s20) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s15, s24) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s17) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s18) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s16, s19) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h28) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h29) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s17, h30) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h31) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h32) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s18, h33) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h34) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h35) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s19, h36) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s21) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s22) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s20, s23) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h37) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h38) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s21, h39) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h40) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h41) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s22, h42) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h43) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h44) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s23, h45) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s25) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s26) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s24, s27) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h46) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h47) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s25, h48) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h49) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h50) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s26, h51) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h52) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h53) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s27, h54) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s29) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s33) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s28, s37) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s30) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s31) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s29, s32) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h55) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h56) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s30, h57) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h58) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h59) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s31, h60) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h61) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h62) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s32, h63) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s34) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s35) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s33, s36) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h64) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h65) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s34, h66) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h67) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h68) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s35, h69) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h70) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h71) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s36, h72) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s38) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s39) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s37, s40) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h73) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h74) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s38, h75) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h76) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h77) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s39, h78) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h79) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h80) (25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.
(25.00Mbit) *** Error: Warning: sch_htb: quantum of class 50001 is big. Consider r2q change.

*** Starting CLI:
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
From 10.0.0.1 icmp_seq=1 Destination Host Unreachable
From 10.0.0.1 icmp_seq=2 Destination Host Unreachable
From 10.0.0.1 icmp_seq=3 Destination Host Unreachable

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 0 received, +3 errors, 100% packet loss, time 2029ms
pipe 3
mininet> h1 ping -c 3 h81
PING 10.0.0.81 (10.0.0.81) 56(84) bytes of data.
64 bytes from 10.0.0.81: icmp_seq=1 ttl=64 time=6.42 ms
64 bytes from 10.0.0.81: icmp_seq=2 ttl=64 time=1.73 ms
64 bytes from 10.0.0.81: icmp_seq=3 ttl=64 time=1.41 ms

--- 10.0.0.81 ping statistics ---
3 packets transmitted, 3 received, 0% packet loss, time 2004ms
rtt min/avg/max/mdev = 1.413/3.186/6.418/2.288 ms
mininet> h1 iperf -s -p 5555 &
mininet> py h1.IP()
10.0.0.1
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 33610 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/1055)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  4.25 MBytes  35.7 Mbits/sec
[  1] 1.0000-2.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 2.0000-3.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 3.0000-4.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 4.0000-5.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 5.0000-6.0000 sec  2.25 MBytes  18.9 Mbits/sec
[  1] 6.0000-7.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 7.0000-8.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 8.0000-9.0000 sec  2.88 MBytes  24.1 Mbits/sec
[  1] 9.0000-10.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 10.0000-11.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 11.0000-12.0000 sec  2.25 MBytes  18.9 Mbits/sec
[  1] 12.0000-13.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 13.0000-14.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 14.0000-15.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 15.0000-16.0000 sec  2.88 MBytes  24.1 Mbits/sec
[  1] 16.0000-17.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 17.0000-18.0000 sec  2.25 MBytes  18.9 Mbits/sec
[  1] 18.0000-19.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 19.0000-20.0000 sec  3.00 MBytes  25.2 Mbits/sec
[  1] 20.0000-20.6661 sec   128 KBytes  1.57 Mbits/sec
[  1] 0.0000-20.6661 sec  58.9 MBytes  23.9 Mbits/sec
mininet> exit
*** Stopping 1 controllers
c0
*** Stopping 120 links
........................................................................................................................
*** Stopping 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Stopping 81 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Done
completed in 112.161 seconds
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=10
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(10.00Mbit) (10.00Mbit) (s1, s2) (10.00Mbit) (10.00Mbit) (s1, s15) (10.00Mbit) (10.00Mbit) (s1, s28) (10.00Mbit) (10.00Mbit) (s2, s3) (10.00Mbit) (10.00Mbit) (s2, s7) (10.00Mbit) (10.00Mbit) (s2, s11) (10.00Mbit) (10.00Mbit) (s3, s4) (10.00Mbit) (10.00Mbit) (s3, s5) (10.00Mbit) (10.00Mbit) (s3, s6) (10.00Mbit) (10.00Mbit) (s4, h1) (10.00Mbit) (10.00Mbit) (s4, h2) (10.00Mbit) (10.00Mbit) (s4, h3) (10.00Mbit) (10.00Mbit) (s5, h4) (10.00Mbit) (10.00Mbit) (s5, h5) (10.00Mbit) (10.00Mbit) (s5, h6) (10.00Mbit) (10.00Mbit) (s6, h7) (10.00Mbit) (10.00Mbit) (s6, h8) (10.00Mbit) (10.00Mbit) (s6, h9) (10.00Mbit) (10.00Mbit) (s7, s8) (10.00Mbit) (10.00Mbit) (s7, s9) (10.00Mbit) (10.00Mbit) (s7, s10) (10.00Mbit) (10.00Mbit) (s8, h10) (10.00Mbit) (10.00Mbit) (s8, h11) (10.00Mbit) (10.00Mbit) (s8, h12) (10.00Mbit) (10.00Mbit) (s9, h13) (10.00Mbit) (10.00Mbit) (s9, h14) (10.00Mbit) (10.00Mbit) (s9, h15) (10.00Mbit) (10.00Mbit) (s10, h16) (10.00Mbit) (10.00Mbit) (s10, h17) (10.00Mbit) (10.00Mbit) (s10, h18) (10.00Mbit) (10.00Mbit) (s11, s12) (10.00Mbit) (10.00Mbit) (s11, s13) (10.00Mbit) (10.00Mbit) (s11, s14) (10.00Mbit) (10.00Mbit) (s12, h19) (10.00Mbit) (10.00Mbit) (s12, h20) (10.00Mbit) (10.00Mbit) (s12, h21) (10.00Mbit) (10.00Mbit) (s13, h22) (10.00Mbit) (10.00Mbit) (s13, h23) (10.00Mbit) (10.00Mbit) (s13, h24) (10.00Mbit) (10.00Mbit) (s14, h25) (10.00Mbit) (10.00Mbit) (s14, h26) (10.00Mbit) (10.00Mbit) (s14, h27) (10.00Mbit) (10.00Mbit) (s15, s16) (10.00Mbit) (10.00Mbit) (s15, s20) (10.00Mbit) (10.00Mbit) (s15, s24) (10.00Mbit) (10.00Mbit) (s16, s17) (10.00Mbit) (10.00Mbit) (s16, s18) (10.00Mbit) (10.00Mbit) (s16, s19) (10.00Mbit) (10.00Mbit) (s17, h28) (10.00Mbit) (10.00Mbit) (s17, h29) (10.00Mbit) (10.00Mbit) (s17, h30) (10.00Mbit) (10.00Mbit) (s18, h31) (10.00Mbit) (10.00Mbit) (s18, h32) (10.00Mbit) (10.00Mbit) (s18, h33) (10.00Mbit) (10.00Mbit) (s19, h34) (10.00Mbit) (10.00Mbit) (s19, h35) (10.00Mbit) (10.00Mbit) (s19, h36) (10.00Mbit) (10.00Mbit) (s20, s21) (10.00Mbit) (10.00Mbit) (s20, s22) (10.00Mbit) (10.00Mbit) (s20, s23) (10.00Mbit) (10.00Mbit) (s21, h37) (10.00Mbit) (10.00Mbit) (s21, h38) (10.00Mbit) (10.00Mbit) (s21, h39) (10.00Mbit) (10.00Mbit) (s22, h40) (10.00Mbit) (10.00Mbit) (s22, h41) (10.00Mbit) (10.00Mbit) (s22, h42) (10.00Mbit) (10.00Mbit) (s23, h43) (10.00Mbit) (10.00Mbit) (s23, h44) (10.00Mbit) (10.00Mbit) (s23, h45) (10.00Mbit) (10.00Mbit) (s24, s25) (10.00Mbit) (10.00Mbit) (s24, s26) (10.00Mbit) (10.00Mbit) (s24, s27) (10.00Mbit) (10.00Mbit) (s25, h46) (10.00Mbit) (10.00Mbit) (s25, h47) (10.00Mbit) (10.00Mbit) (s25, h48) (10.00Mbit) (10.00Mbit) (s26, h49) (10.00Mbit) (10.00Mbit) (s26, h50) (10.00Mbit) (10.00Mbit) (s26, h51) (10.00Mbit) (10.00Mbit) (s27, h52) (10.00Mbit) (10.00Mbit) (s27, h53) (10.00Mbit) (10.00Mbit) (s27, h54) (10.00Mbit) (10.00Mbit) (s28, s29) (10.00Mbit) (10.00Mbit) (s28, s33) (10.00Mbit) (10.00Mbit) (s28, s37) (10.00Mbit) (10.00Mbit) (s29, s30) (10.00Mbit) (10.00Mbit) (s29, s31) (10.00Mbit) (10.00Mbit) (s29, s32) (10.00Mbit) (10.00Mbit) (s30, h55) (10.00Mbit) (10.00Mbit) (s30, h56) (10.00Mbit) (10.00Mbit) (s30, h57) (10.00Mbit) (10.00Mbit) (s31, h58) (10.00Mbit) (10.00Mbit) (s31, h59) (10.00Mbit) (10.00Mbit) (s31, h60) (10.00Mbit) (10.00Mbit) (s32, h61) (10.00Mbit) (10.00Mbit) (s32, h62) (10.00Mbit) (10.00Mbit) (s32, h63) (10.00Mbit) (10.00Mbit) (s33, s34) (10.00Mbit) (10.00Mbit) (s33, s35) (10.00Mbit) (10.00Mbit) (s33, s36) (10.00Mbit) (10.00Mbit) (s34, h64) (10.00Mbit) (10.00Mbit) (s34, h65) (10.00Mbit) (10.00Mbit) (s34, h66) (10.00Mbit) (10.00Mbit) (s35, h67) (10.00Mbit) (10.00Mbit) (s35, h68) (10.00Mbit) (10.00Mbit) (s35, h69) (10.00Mbit) (10.00Mbit) (s36, h70) (10.00Mbit) (10.00Mbit) (s36, h71) (10.00Mbit) (10.00Mbit) (s36, h72) (10.00Mbit) (10.00Mbit) (s37, s38) (10.00Mbit) (10.00Mbit) (s37, s39) (10.00Mbit) (10.00Mbit) (s37, s40) (10.00Mbit) (10.00Mbit) (s38, h73) (10.00Mbit) (10.00Mbit) (s38, h74) (10.00Mbit) (10.00Mbit) (s38, h75) (10.00Mbit) (10.00Mbit) (s39, h76) (10.00Mbit) (10.00Mbit) (s39, h77) (10.00Mbit) (10.00Mbit) (s39, h78) (10.00Mbit) (10.00Mbit) (s40, h79) (10.00Mbit) (10.00Mbit) (s40, h80) (10.00Mbit) (10.00Mbit) (s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit) (10.00Mbit)
*** Starting CLI:
mininet> py h1.IP()
10.0.0.1
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 60952 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/1556)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  3.38 MBytes  28.3 Mbits/sec
[  1] 1.0000-2.0000 sec  1.12 MBytes  9.42 Mbits/sec
[  1] 2.0000-3.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 3.0000-4.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 4.0000-5.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 5.0000-6.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 6.0000-7.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 7.0000-8.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 8.0000-9.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 9.0000-10.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 10.0000-11.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 11.0000-12.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 12.0000-13.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 13.0000-14.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 14.0000-15.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 15.0000-16.0000 sec  1.12 MBytes  9.38 Mbits/sec
[  1] 16.0000-17.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 17.0000-18.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 18.0000-19.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 19.0000-20.0000 sec  1.18 MBytes  9.90 Mbits/sec
[  1] 20.0000-21.8800 sec  60.7 KBytes   264 Kbits/sec
[  1] 0.0000-21.8800 sec  25.0 MBytes  9.59 Mbits/sec
mininet> exit
*** Stopping 1 controllers
c0
*** Stopping 120 links
........................................................................................................................
*** Stopping 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Stopping 81 hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Done
completed in 79.383 seconds
cplusplus@Galisse:~$ sudo mn --topo tree,depth=4,fanout=3 --mac --link tc,bw=5
*** Creating network
*** Adding controller
*** Adding hosts:
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Adding switches:
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40
*** Adding links:
(5.00Mbit) (5.00Mbit) (s1, s2) (5.00Mbit) (5.00Mbit) (s1, s15) (5.00Mbit) (5.00Mbit) (s1, s28) (5.00Mbit) (5.00Mbit) (s2, s3) (5.00Mbit) (5.00Mbit) (s2, s7) (5.00Mbit) (5.00Mbit) (s2, s11) (5.00Mbit) (5.00Mbit) (s3, s4) (5.00Mbit) (5.00Mbit) (s3, s5) (5.00Mbit) (5.00Mbit) (s3, s6) (5.00Mbit) (5.00Mbit) (s4, h1) (5.00Mbit) (5.00Mbit) (s4, h2) (5.00Mbit) (5.00Mbit) (s4, h3) (5.00Mbit) (5.00Mbit) (s5, h4) (5.00Mbit) (5.00Mbit) (s5, h5) (5.00Mbit) (5.00Mbit) (s5, h6) (5.00Mbit) (5.00Mbit) (s6, h7) (5.00Mbit) (5.00Mbit) (s6, h8) (5.00Mbit) (5.00Mbit) (s6, h9) (5.00Mbit) (5.00Mbit) (s7, s8) (5.00Mbit) (5.00Mbit) (s7, s9) (5.00Mbit) (5.00Mbit) (s7, s10) (5.00Mbit) (5.00Mbit) (s8, h10) (5.00Mbit) (5.00Mbit) (s8, h11) (5.00Mbit) (5.00Mbit) (s8, h12) (5.00Mbit) (5.00Mbit) (s9, h13) (5.00Mbit) (5.00Mbit) (s9, h14) (5.00Mbit) (5.00Mbit) (s9, h15) (5.00Mbit) (5.00Mbit) (s10, h16) (5.00Mbit) (5.00Mbit) (s10, h17) (5.00Mbit) (5.00Mbit) (s10, h18) (5.00Mbit) (5.00Mbit) (s11, s12) (5.00Mbit) (5.00Mbit) (s11, s13) (5.00Mbit) (5.00Mbit) (s11, s14) (5.00Mbit) (5.00Mbit) (s12, h19) (5.00Mbit) (5.00Mbit) (s12, h20) (5.00Mbit) (5.00Mbit) (s12, h21) (5.00Mbit) (5.00Mbit) (s13, h22) (5.00Mbit) (5.00Mbit) (s13, h23) (5.00Mbit) (5.00Mbit) (s13, h24) (5.00Mbit) (5.00Mbit) (s14, h25) (5.00Mbit) (5.00Mbit) (s14, h26) (5.00Mbit) (5.00Mbit) (s14, h27) (5.00Mbit) (5.00Mbit) (s15, s16) (5.00Mbit) (5.00Mbit) (s15, s20) (5.00Mbit) (5.00Mbit) (s15, s24) (5.00Mbit) (5.00Mbit) (s16, s17) (5.00Mbit) (5.00Mbit) (s16, s18) (5.00Mbit) (5.00Mbit) (s16, s19) (5.00Mbit) (5.00Mbit) (s17, h28) (5.00Mbit) (5.00Mbit) (s17, h29) (5.00Mbit) (5.00Mbit) (s17, h30) (5.00Mbit) (5.00Mbit) (s18, h31) (5.00Mbit) (5.00Mbit) (s18, h32) (5.00Mbit) (5.00Mbit) (s18, h33) (5.00Mbit) (5.00Mbit) (s19, h34) (5.00Mbit) (5.00Mbit) (s19, h35) (5.00Mbit) (5.00Mbit) (s19, h36) (5.00Mbit) (5.00Mbit) (s20, s21) (5.00Mbit) (5.00Mbit) (s20, s22) (5.00Mbit) (5.00Mbit) (s20, s23) (5.00Mbit) (5.00Mbit) (s21, h37) (5.00Mbit) (5.00Mbit) (s21, h38) (5.00Mbit) (5.00Mbit) (s21, h39) (5.00Mbit) (5.00Mbit) (s22, h40) (5.00Mbit) (5.00Mbit) (s22, h41) (5.00Mbit) (5.00Mbit) (s22, h42) (5.00Mbit) (5.00Mbit) (s23, h43) (5.00Mbit) (5.00Mbit) (s23, h44) (5.00Mbit) (5.00Mbit) (s23, h45) (5.00Mbit) (5.00Mbit) (s24, s25) (5.00Mbit) (5.00Mbit) (s24, s26) (5.00Mbit) (5.00Mbit) (s24, s27) (5.00Mbit) (5.00Mbit) (s25, h46) (5.00Mbit) (5.00Mbit) (s25, h47) (5.00Mbit) (5.00Mbit) (s25, h48) (5.00Mbit) (5.00Mbit) (s26, h49) (5.00Mbit) (5.00Mbit) (s26, h50) (5.00Mbit) (5.00Mbit) (s26, h51) (5.00Mbit) (5.00Mbit) (s27, h52) (5.00Mbit) (5.00Mbit) (s27, h53) (5.00Mbit) (5.00Mbit) (s27, h54) (5.00Mbit) (5.00Mbit) (s28, s29) (5.00Mbit) (5.00Mbit) (s28, s33) (5.00Mbit) (5.00Mbit) (s28, s37) (5.00Mbit) (5.00Mbit) (s29, s30) (5.00Mbit) (5.00Mbit) (s29, s31) (5.00Mbit) (5.00Mbit) (s29, s32) (5.00Mbit) (5.00Mbit) (s30, h55) (5.00Mbit) (5.00Mbit) (s30, h56) (5.00Mbit) (5.00Mbit) (s30, h57) (5.00Mbit) (5.00Mbit) (s31, h58) (5.00Mbit) (5.00Mbit) (s31, h59) (5.00Mbit) (5.00Mbit) (s31, h60) (5.00Mbit) (5.00Mbit) (s32, h61) (5.00Mbit) (5.00Mbit) (s32, h62) (5.00Mbit) (5.00Mbit) (s32, h63) (5.00Mbit) (5.00Mbit) (s33, s34) (5.00Mbit) (5.00Mbit) (s33, s35) (5.00Mbit) (5.00Mbit) (s33, s36) (5.00Mbit) (5.00Mbit) (s34, h64) (5.00Mbit) (5.00Mbit) (s34, h65) (5.00Mbit) (5.00Mbit) (s34, h66) (5.00Mbit) (5.00Mbit) (s35, h67) (5.00Mbit) (5.00Mbit) (s35, h68) (5.00Mbit) (5.00Mbit) (s35, h69) (5.00Mbit) (5.00Mbit) (s36, h70) (5.00Mbit) (5.00Mbit) (s36, h71) (5.00Mbit) (5.00Mbit) (s36, h72) (5.00Mbit) (5.00Mbit) (s37, s38) (5.00Mbit) (5.00Mbit) (s37, s39) (5.00Mbit) (5.00Mbit) (s37, s40) (5.00Mbit) (5.00Mbit) (s38, h73) (5.00Mbit) (5.00Mbit) (s38, h74) (5.00Mbit) (5.00Mbit) (s38, h75) (5.00Mbit) (5.00Mbit) (s39, h76) (5.00Mbit) (5.00Mbit) (s39, h77) (5.00Mbit) (5.00Mbit) (s39, h78) (5.00Mbit) (5.00Mbit) (s40, h79) (5.00Mbit) (5.00Mbit) (s40, h80) (5.00Mbit) (5.00Mbit) (s40, h81)
*** Configuring hosts
h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 h11 h12 h13 h14 h15 h16 h17 h18 h19 h20 h21 h22 h23 h24 h25 h26 h27 h28 h29 h30 h31 h32 h33 h34 h35 h36 h37 h38 h39 h40 h41 h42 h43 h44 h45 h46 h47 h48 h49 h50 h51 h52 h53 h54 h55 h56 h57 h58 h59 h60 h61 h62 h63 h64 h65 h66 h67 h68 h69 h70 h71 h72 h73 h74 h75 h76 h77 h78 h79 h80 h81
*** Starting controller
c0
*** Starting 40 switches
s1 s2 s3 s4 s5 s6 s7 s8 s9 s10 s11 s12 s13 s14 s15 s16 s17 s18 s19 s20 s21 s22 s23 s24 s25 s26 s27 s28 s29 s30 s31 s32 s33 s34 s35 s36 s37 s38 s39 s40 ...(5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit) (5.00Mbit)
*** Starting CLI:
mininet> h1 iperf -s -p 5555 &
mininet> h2 iperf -c 10.0.0.1 -p 5555 -i 1 -t 20
------------------------------------------------------------
Client connecting to 10.0.0.1, TCP port 5555
TCP window size: 85.3 KByte (default)
------------------------------------------------------------
[  1] local 10.0.0.2 port 44796 connected with 10.0.0.1 port 5555 (icwnd/mss/irtt=14/1448/2339)
[ ID] Interval       Transfer     Bandwidth
[  1] 0.0000-1.0000 sec  2.88 MBytes  24.1 Mbits/sec
[  1] 1.0000-2.0000 sec   580 KBytes  4.75 Mbits/sec
[  1] 2.0000-3.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 3.0000-4.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 4.0000-5.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 5.0000-6.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 6.0000-7.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 7.0000-8.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 8.0000-9.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 9.0000-10.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 10.0000-11.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 11.0000-12.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 12.0000-13.0000 sec   318 KBytes  2.61 Mbits/sec
[  1] 13.0000-14.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 14.0000-15.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 15.0000-16.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 16.0000-17.0000 sec   508 KBytes  4.16 Mbits/sec
[  1] 17.0000-18.0000 sec   701 KBytes  5.74 Mbits/sec
[  1] 18.0000-19.0000 sec   573 KBytes  4.69 Mbits/sec
[  1] 19.0000-20.0000 sec   636 KBytes  5.21 Mbits/sec
[  1] 20.0000-25.0234 sec  62.2 KBytes   101 Kbits/sec
[  1] 0.0000-25.0234 sec  13.8 MBytes  4.61 Mbits/sec
```