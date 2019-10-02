$# LS-DYNA Keyword file created by LS-PrePost(R) V4.6.3 - 11Feb2019
$# Created on Apr-09-2019 (21:07:13)
*KEYWORD
*TITLE
$#                                                                         title
LS-DYNA keyword deck by LS-PrePost
*CONTROL_ENERGY
$#    hgen      rwen    slnten     rylen     
         1         2         1         1
*CONTROL_HOURGLASS
$#     ihq        qh  
         1       0.1
*CONTROL_SOLID
$#   esort   fmatrix   niptets    swlocl    psfail   t10jtol    icohed    tet13k
         0         0         4         1         0       0.0         0         0
$#   pm1     pm2     pm3     pm4     pm5     pm6     pm7     pm8     pm9    pm10
       0       0       0       0       0       0       0       0       0       0
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
*SET_NODE_LIST
$#     sid       da1       da2       da3       da4    solver      
         4       0.0       0.0       0.0       0.0MECH
$#    nid1      nid2      nid3      nid4      nid5      nid6      nid7      nid8
         6         8         5         7         0         0         0         0
*DATABASE_ELOUT
$#      dt    binary      lcur     ioopt   option1   option2   option3   option4
    1.0e-2         0         0         1         8         0         0         0
*DATABASE_BINARY_D3PLOT
$#      dt      lcdt      beam     npltc    psetid      
       0.1         0         0         0         0
$#   ioopt     
         0
*DATABASE_EXTENT_BINARY
$    NEIPH     NEIPS    MAXINT    STRFLG    SIGFLG    EPSFLG    RLTFLG    ENGFLG
$#   neiph     neips    maxint    strflg    sigflg    epsflg    rltflg    engflg
         9         9         3         1         1         1         1         1
$
$#  cmpflg    ieverp    beamip     dcomp      shge     stssz    n3thdt   ialemat
         0         0         0         1         1         1         2         1
*DATABASE_HISTORY_SOLID
$#     id1       id2       id3       id4       id5       id6       id7       id8
         1         0         0         0         0         0         0         0
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
*MAT_ORTHOTROPIC_SIMPLIFIED_DAMAGE
$ из статьи Сергеичева
$#     mid        ro        ea        eb        ec      prba      prca      prcb
         1   0.00150  157000.0    8500.0    8500.0    0.0189    0.0287      0.35
$#     gab       gbc       gca    unused      aopt      macf
    4200.0    2200.0    4200.0                 0.0         1
$#      xp        yp        zp        a1        a2        a3
       0.0       0.0       0.0       0.0       0.0       0.0
$#      v1        v2        v3        d1        d2        d3      beta
       0.0       0.0       0.0       0.0       0.0       0.0       0.0
$#  nerode      ndam    eps1tf    eps2tf    eps3tf    eps1cf    eps2cf    eps3cf
{nerode: 10d}{ndam:10d}1.00000E201.00000E201.00000E20-1.0000E20-1.0000E20-1.0000E20
$#  eps12f    eps23f    eps13f    epsd1t    epsc1t    cdam1t    epsd2t    epsc2t
1.00000E201.00000E201.00000E20      0.01      0.02       1.0      0.01      0.02
$#  cdam2t    epsd3t    epsc3t    cdam3t    epsd1c    epsc1c    cdam1c    epsd2c
       1.0      0.01      0.02       1.0    -0.007     -0.01       1.0     -0.01
$#  epsc2c    cdam2c    epsd3c    epsc3c    cdam3c    epsd12    epsc12    cdam12
     -0.02       1.0     -0.01     -0.02      1.0      0.015      0.03       1.0
$#  epsd23    epsc23    cdam23    epsd31    epsc31    cdam31
     0.015      0.03       1.0     0.015      0.03       1.0
$
*PART
$#                                                                         title
cub
$#     pid     secid       mid     eosid      hgid      grav    adpopt      tmid
         1         1         1         0         0         0         0         0
*END
