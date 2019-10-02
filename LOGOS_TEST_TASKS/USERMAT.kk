$# LS-DYNA Keyword file created by LS-PrePost(R) V4.6.3 - 11Feb2019
$# Created on Apr-09-2019 (21:07:13)
*KEYWORD
*TITLE
$#                                                                         title
LS-DYNA keyword deck by LS-PrePost
*CONTROL_HOURGLASS
$#     ihq        qh  
         1       0.1
*CONTROL_TERMINATION
$#  endtim    endcyc     dtmin    endeng    endmas     nosol     
       1.0         0       0.0       0.01.000000E8         0
*CONTROL_TIMESTEP
$#  dtinit    tssfac      isdo    tslimt     dt2ms      lctm     erode     ms1st
       0.0       0.1         0       0.0       0.0         0         0         0
$#  dt2msf   dt2mslc     imscl    unused    unused     rmscl     
       0.0         0         0                           0.0
$
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         1       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         4         2         3         1         0         0         0         0
*BOUNDARY_SPC_SET
$#    nsid       cid      dofx      dofy      dofz     dofrx     dofry     dofrz
         4         0         0         1         1         0         0         0
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         4       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         6         8         5         7         0         0         0         0
*DATABASE_BINARY_D3PLOT
$#      dt      lcdt      beam     npltc    psetid      
     0.003         0         0         0         0
$#   ioopt     
         0
*DATABASE_EXTENT_BINARY
$    NEIPH     NEIPS    MAXINT    STRFLG    SIGFLG    EPSFLG    RLTFLG    ENGFLG
$#   neiph     neips    maxint    strflg    sigflg    epsflg    rltflg    engflg
         0         0         3         1         1         1         1         1
$
$#  cmpflg    ieverp    beamip     dcomp      shge     stssz    n3thdt   ialemat
         0         0         0         1         1         1         2         1
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         2       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         2         6         1         5         0         0         0         0
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         3       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         1         5         7         3         0         0         0         0
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         5       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         8         4         7         3         0         0         0         0
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         6       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         8         4         2         6         0         0         0         0
*SET_SEGMENT
$#     sid       da1       da2       da3       da4    solver      
         1       0.0       0.0       0.0       0.0MECH
$#      n1        n2        n3        n4        a1        a2        a3        a4
         5         7         8         6       0.0       0.0       0.0       0.0
*SET_SEGMENT
$#     sid       da1       da2       da3       da4    solver      
         2       0.0       0.0       0.0       0.0MECH
$#      n1        n2        n3        n4        a1        a2        a3        a4
         3         4         8         7       0.0       0.0       0.0       0.0
*SET_SEGMENT
$#     sid       da1       da2       da3       da4    solver      
         3       0.0       0.0       0.0       0.0MECH
$#      n1        n2        n3        n4        a1        a2        a3        a4
         8         4         2         6       0.0       0.0       0.0       0.0
*ELEMENT_SOLID
$#   eid     pid      n1      n2      n3      n4      n5      n6      n7      n8
       1       1       1       5       7       3       2       6       8       4
*NODE
$#   nid               x               y               z      tc      rc  
       1             0.0             0.0             0.0       0       0
       2             0.0             0.0             1.0       0       0
       3             0.0             1.0             0.0       0       0
       4             0.0             1.0             1.0       0       0
       5             1.0             0.0             0.0       0       0
       6             1.0             0.0             1.0       0       0
       7             1.0             1.0             0.0       0       0
       8             1.0             1.0             1.0       0       0
*SECTION_SOLID
$#   secid    elform       aet   
         1         1         0
*MAT_USER_DEFINED_MATERIAL_MODELS
$#     mid        ro        mt       lmc       nhv    iortho     ibulk        ig
         1   0.00150         0        47        15         1         0         0
$#   ivect     ifail    itherm    ihyper      ieos      lmca    unused    unused
         0         0         0         0         0         0                    
$#    aopt      mafc        xp        yp        zp        a1        a2        a3
         0       1.0       0.0       0.0       0.0       0.0       0.0       0.0
$#      v1        v2        v3        d1        d2        d3      beta     ievts
       0.0       0.0       0.0       0.0       0.0       0.0       0.0        15
$#      ea        eb        ec      prba      prca      prcb       gab       gbc       
$#      E1        E2        E2      PR21      PR31      PR32       G12       G23       
$#      p1        p2        p3        p4        p5        p6        p7        p8
  157000.0    8500.0    8500.0    0.0189    0.0287      0.35    4200.0    2200.0
$#     gca    nerode      ndam    eps1tf    eps2tf    eps3tf    eps1cf    eps2cf
$#     G31    nerode      ndam      e1tf      e2tf      e3tf      e1cf      e2cf
$#      p9       p10       p11       p12       p13       p14       p15       p16
    4200.0{nerode: 10d}{ndam:10d}      1e201.00000E201.00000E20     -1e20-1.0000E20
$#  eps3cf    eps12f    eps23f    eps13f    epsd1t    epsc1t    cdam1t    epsd2t
$#    e3cf      e12f      e23f      e13f      e1ts      e1tc       D1t      e2ts
$#     p17       p18       p19       p20       p21       p22       p23       p24
-1.0000E201.00000E201.00000E201.00000E20      0.01      0.02       1.0      0.01
$#  epsc2t    cdam2t    epsd3t    epsc3t    cdam3t    epsd1c    epsc1c    cdam1c
$#    e2tc       D2t      e3ts      e3tc       D3t      e1cs      e1cc       D1c
$#     p25       p26       p27       p28       p29       p30       p31       p32
      0.02       1.0      0.01      0.02       1.0    -0.007     -0.01       1.0
$#  epsd2c    epsc2c    cdam2c    epsd3c    epsc3c    cdam3c    epsd12    epsc12
$#    e2cs      e2cc       D2c      e3cs      e3cc       D3c      e12s      e12c
$#     p33       p34       p35       p36       p37       p38       p39       p40
     -0.01     -0.02       1.0     -0.01     -0.02       1.0     0.015      0.03
$#  cdam12    epsd23    epsc23    cdam23    epsd31    epsc31    cdam31
$#     D12      e23s      e23c       D23      e13s      e13c       D13
$#     p41       p42       p43       p44       p45       p46       p47       p48
       1.0     0.015      0.03       1.0     0.015      0.03       1.0
$
$
*PART
$#                                                                         title
cub
$#     pid     secid       mid     eosid      hgid      grav    adpopt      tmid
         1         1         1         0         0         0         0         0
*END
