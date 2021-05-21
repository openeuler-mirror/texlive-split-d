%global tl_version 2018
%global _texdir %{_datadir}/texlive
%global __brp_mangle_shebangs /usr/bin/true

Name:           texlive-split-d
Version:        %{tl_version}
Release:        24
Epoch:          8
Summary:        TeX formatting system
License:        Artistic 2.0 and GPLv2 and GPLv2+ and LGPLv2+ and LPPL and MIT and Public Domain and UCD and Utopia
URL:            http://tug.org/texlive/
BuildArch:      noarch
Source0003:     texlive-licenses.tar.xz
Source0859:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blacklettert1.tar.xz
Source0860:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blacklettert1.doc.tar.xz
Source0862:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blindtext.tar.xz
Source0863:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blindtext.doc.tar.xz
Source0865:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blkarray.tar.xz
Source0866:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blkarray.doc.tar.xz
Source0867:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blochsphere.tar.xz
Source0868:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blochsphere.doc.tar.xz
Source0870:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blockdraw_mp.tar.xz
Source0871:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blockdraw_mp.doc.tar.xz
Source0872:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/block.tar.xz
Source0873:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/block.doc.tar.xz
Source0874:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bloques.tar.xz
Source0875:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bloques.doc.tar.xz
Source0879:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blox.tar.xz
Source0880:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/blox.doc.tar.xz
Source0882:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bnumexpr.tar.xz
Source0883:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bnumexpr.doc.tar.xz
Source0885:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bodegraph.tar.xz
Source0886:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bodegraph.doc.tar.xz
Source0887:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bohr.tar.xz
Source0888:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bohr.doc.tar.xz
Source0889:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boisik.tar.xz
Source0890:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boisik.doc.tar.xz
Source0891:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boites.tar.xz
Source0892:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boites.doc.tar.xz
Source0894:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bold-extra.tar.xz
Source0895:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bold-extra.doc.tar.xz
Source0896:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boldtensors.tar.xz
Source0897:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boldtensors.doc.tar.xz
Source0898:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bondgraphs.tar.xz
Source0899:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bondgraphs.doc.tar.xz
Source0901:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bondgraph.tar.xz
Source0902:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bondgraph.doc.tar.xz
Source0903:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookcover.tar.xz
Source0904:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookcover.doc.tar.xz
Source0906:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookdb.tar.xz
Source0907:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookdb.doc.tar.xz
Source0908:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookest.tar.xz
Source0909:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookest.doc.tar.xz
Source0910:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookhands.tar.xz
Source0911:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookhands.doc.tar.xz
Source0913:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/booklet.tar.xz
Source0914:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/booklet.doc.tar.xz
Source0916:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bookman.tar.xz
Source0917:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/booktabs-de.doc.tar.xz
Source0918:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/booktabs-fr.doc.tar.xz
Source0919:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/booktabs.tar.xz
Source0920:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/booktabs.doc.tar.xz
Source0922:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boolexpr.tar.xz
Source0923:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boolexpr.doc.tar.xz
Source0925:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boondox.tar.xz
Source0926:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boondox.doc.tar.xz
Source0927:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bophook.tar.xz
Source0928:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bophook.doc.tar.xz
Source0930:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/borceux.tar.xz
Source0931:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/borceux.doc.tar.xz
Source0932:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bosisio.tar.xz
Source0933:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bosisio.doc.tar.xz
Source0935:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boxedminipage2e.tar.xz
Source0936:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boxedminipage2e.doc.tar.xz
Source0938:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boxedminipage.tar.xz
Source0939:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boxedminipage.doc.tar.xz
Source0940:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boxhandler.tar.xz
Source0941:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/boxhandler.doc.tar.xz
Source0943:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bpchem.tar.xz
Source0944:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bpchem.doc.tar.xz
Source0946:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bpolynomial.tar.xz
Source0947:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bpolynomial.doc.tar.xz
Source0948:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bracketkey.tar.xz
Source0949:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bracketkey.doc.tar.xz
Source0950:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/braids.tar.xz
Source0951:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/braids.doc.tar.xz
Source0953:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/braille.tar.xz
Source0954:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/braille.doc.tar.xz
Source0955:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/braket.tar.xz
Source0956:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/braket.doc.tar.xz
Source0957:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/brandeis-dissertation.tar.xz
Source0958:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/brandeis-dissertation.doc.tar.xz
Source0960:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/breakurl.tar.xz
Source0961:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/breakurl.doc.tar.xz
Source0963:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/breqn.tar.xz
Source0964:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/breqn.doc.tar.xz
Source0966:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/br-lex.tar.xz
Source0967:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/br-lex.doc.tar.xz
Source0968:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bropd.tar.xz
Source0969:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bropd.doc.tar.xz
Source0971:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/brushscr.tar.xz
Source0972:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/brushscr.doc.tar.xz
Source0973:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bullcntr.tar.xz
Source0974:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bullcntr.doc.tar.xz
Source0978:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/burmese.tar.xz
Source0979:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/burmese.doc.tar.xz
Source0981:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bussproofs.tar.xz
Source0982:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bussproofs.doc.tar.xz
Source0983:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxbase.tar.xz
Source0984:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxbase.doc.tar.xz
Source0985:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxcjkjatype.tar.xz
Source0986:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxcjkjatype.doc.tar.xz
Source0987:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxdpx-beamer.tar.xz
Source0988:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxdpx-beamer.doc.tar.xz
Source0989:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxeepic.tar.xz
Source0990:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxeepic.doc.tar.xz
Source0991:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxjscls.tar.xz
Source0992:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxjscls.doc.tar.xz
Source0994:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxpdfver.tar.xz
Source0995:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxpdfver.doc.tar.xz
Source0996:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bytefield.tar.xz
Source0997:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bytefield.doc.tar.xz
Source0999:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/c90.tar.xz
Source1000:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/c90.doc.tar.xz
Source1002:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cabin.tar.xz
Source1003:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cabin.doc.tar.xz
Source1006:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/caladea.tar.xz
Source1007:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/caladea.doc.tar.xz
Source1008:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calcage.tar.xz
Source1009:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calcage.doc.tar.xz
Source1011:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calctab.tar.xz
Source1012:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calctab.doc.tar.xz
Source1013:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calculation.tar.xz
Source1014:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calculation.doc.tar.xz
Source1016:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calculator.tar.xz
Source1017:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calculator.doc.tar.xz
Source1019:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calligra.tar.xz
Source1020:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calligra.doc.tar.xz
Source1021:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calligra-type1.tar.xz
Source1022:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calligra-type1.doc.tar.xz
Source1023:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calrsfs.tar.xz
Source1024:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calrsfs.doc.tar.xz
Source1025:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cals.tar.xz
Source1026:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cals.doc.tar.xz
Source1028:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calxxxx-yyyy.tar.xz
Source1029:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/calxxxx-yyyy.doc.tar.xz
Source1030:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cancel.tar.xz
Source1031:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cancel.doc.tar.xz
Source1032:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/canoniclayout.tar.xz
Source1033:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/canoniclayout.doc.tar.xz
Source1035:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cantarell.tar.xz
Source1036:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cantarell.doc.tar.xz
Source1038:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/captcont.tar.xz
Source1039:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/captcont.doc.tar.xz
Source1041:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/captdef.tar.xz
Source1042:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/captdef.doc.tar.xz
Source1043:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/caption.tar.xz
Source1044:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/caption.doc.tar.xz
Source1046:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/capt-of.tar.xz
Source1047:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/capt-of.doc.tar.xz
Source1049:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carlisle.tar.xz
Source1050:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carlisle.doc.tar.xz
Source1052:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carlito.tar.xz
Source1053:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carlito.doc.tar.xz
Source1054:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carolmin-ps.tar.xz
Source1055:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carolmin-ps.doc.tar.xz
Source1056:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cascadilla.tar.xz
Source1057:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cascadilla.doc.tar.xz
Source1058:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cases.tar.xz
Source1059:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cases.doc.tar.xz
Source1060:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/casyl.tar.xz
Source1061:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/casyl.doc.tar.xz
Source1062:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catchfilebetweentags.tar.xz
Source1063:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catchfilebetweentags.doc.tar.xz
Source1065:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catcodes.tar.xz
Source1066:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catcodes.doc.tar.xz
Source1068:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catechis.tar.xz
Source1069:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catechis.doc.tar.xz
Source1071:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catoptions.tar.xz
Source1072:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/catoptions.doc.tar.xz
Source1073:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cbcoptic.tar.xz
Source1074:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cbcoptic.doc.tar.xz
Source1075:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cbfonts-fd.tar.xz
Source1076:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cbfonts-fd.doc.tar.xz
Source1078:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cbfonts.tar.xz
Source1079:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cbfonts.doc.tar.xz
Source1080:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ccaption.tar.xz
Source1081:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ccaption.doc.tar.xz
Source1083:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ccfonts.tar.xz
Source1084:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ccfonts.doc.tar.xz
Source1086:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ccicons.tar.xz
Source1087:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/ccicons.doc.tar.xz
Source1089:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cclicenses.tar.xz
Source1090:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cclicenses.doc.tar.xz
Source1092:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cc-pl.tar.xz
Source1093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cc-pl.doc.tar.xz
Source1094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cd-cover.tar.xz
Source1095:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cd-cover.doc.tar.xz
Source1097:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cdpbundl.tar.xz
Source1098:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cdpbundl.doc.tar.xz
Source1100:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cd.tar.xz
Source1101:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cd.doc.tar.xz
Source1103:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cellspace.tar.xz
Source1104:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cellspace.doc.tar.xz
Source1105:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cell.tar.xz
Source1106:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cell.doc.tar.xz
Source1107:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/celtic.tar.xz
Source1108:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/celtic.doc.tar.xz
Source1110:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/censor.tar.xz
Source1111:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/censor.doc.tar.xz
Source1112:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cfr-initials.tar.xz
Source1113:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cfr-initials.doc.tar.xz
Source1114:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cfr-lm.tar.xz
Source1115:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cfr-lm.doc.tar.xz
Source1117:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changebar.tar.xz
Source1118:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changebar.doc.tar.xz
Source1120:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changelayout.tar.xz
Source1121:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changelayout.doc.tar.xz
Source1122:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changepage.tar.xz
Source1123:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changepage.doc.tar.xz
Source1125:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changes.tar.xz
Source1126:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/changes.doc.tar.xz
Source1128:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chappg.tar.xz
Source1129:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chappg.doc.tar.xz
Source1131:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chapterfolder.tar.xz
Source1132:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chapterfolder.doc.tar.xz
Source1134:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/charter.tar.xz
Source1135:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/charter.doc.tar.xz
Source1136:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chbibref.tar.xz
Source1137:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chbibref.doc.tar.xz
Source1143:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemarrow.tar.xz
Source1144:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemarrow.doc.tar.xz
Source1146:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chembst.tar.xz
Source1147:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chembst.doc.tar.xz
Source1149:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemcompounds.tar.xz
Source1150:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemcompounds.doc.tar.xz
Source1152:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemcono.tar.xz
Source1153:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemcono.doc.tar.xz
Source1154:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemexec.tar.xz
Source1155:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemexec.doc.tar.xz
Source1156:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemfig.tar.xz
Source1157:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemfig.doc.tar.xz
Source1158:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemformula.tar.xz
Source1159:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemformula.doc.tar.xz
Source1160:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemgreek.tar.xz
Source1161:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemgreek.doc.tar.xz
Source1162:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chem-journal.tar.xz
Source1163:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemmacros.tar.xz
Source1164:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemmacros.doc.tar.xz
Source1165:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemnum.tar.xz
Source1166:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemnum.doc.tar.xz
Source1167:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemschemex.tar.xz
Source1168:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemschemex.doc.tar.xz
Source1170:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemstyle.tar.xz
Source1171:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemstyle.doc.tar.xz
Source1173:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cherokee.tar.xz
Source1174:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cherokee.doc.tar.xz
Source1175:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chessboard.tar.xz
Source1176:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chessboard.doc.tar.xz
Source1178:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chessfss.tar.xz
Source1179:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chessfss.doc.tar.xz
Source1181:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chess-problem-diagrams.tar.xz
Source1182:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chess-problem-diagrams.doc.tar.xz
Source1184:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chess.tar.xz
Source1185:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chess.doc.tar.xz
Source1186:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chet.tar.xz
Source1187:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chet.doc.tar.xz
Source1188:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chextras.tar.xz
Source1189:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chextras.doc.tar.xz
Source1191:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chicago-annote.tar.xz
Source1192:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chicago-annote.doc.tar.xz
Source1193:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chicago.tar.xz
Source1194:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chickenize.tar.xz
Source1195:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chickenize.doc.tar.xz
Source1197:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chkfloat.tar.xz
Source1198:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chkfloat.doc.tar.xz
Source1201:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chletter.tar.xz
Source1202:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chletter.doc.tar.xz
Source1204:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chngcntr.tar.xz
Source1205:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chngcntr.doc.tar.xz
Source1206:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chronology.tar.xz
Source1207:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chronology.doc.tar.xz
Source1208:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chronosys.tar.xz
Source1209:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chronosys.doc.tar.xz
Source1210:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chscite.tar.xz
Source1211:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chscite.doc.tar.xz
Source7270:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/breakcites.tar.xz
Source7271:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/breakcites.doc.tar.xz
Source7272:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxdvidriver.tar.xz
Source7273:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxdvidriver.doc.tar.xz
Source7274:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxenclose.tar.xz
Source7275:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxenclose.doc.tar.xz
Source7276:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxnewfont.tar.xz
Source7277:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxnewfont.doc.tar.xz
Source7278:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxpapersize.tar.xz
Source7279:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxpapersize.doc.tar.xz
Source7280:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carbohydrates.tar.xz
Source7281:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/carbohydrates.doc.tar.xz
Source7282:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chivo.tar.xz
Source7283:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chivo.doc.tar.xz
Source7285:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/churchslavonic.tar.xz
Source7286:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/churchslavonic.doc.tar.xz
Source7675:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bredzenie.tar.xz
Source7676:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bredzenie.doc.tar.xz
Source7677:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxcalc.tar.xz
Source7678:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxcalc.doc.tar.xz
Source7679:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxjalipsum.tar.xz
Source7680:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxjalipsum.doc.tar.xz
Source7681:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxjaprnind.tar.xz
Source7682:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxjaprnind.doc.tar.xz
Source7683:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxorigcapt.tar.xz
Source7684:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/bxorigcapt.doc.tar.xz
Source7685:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/callouts.tar.xz
Source7686:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/callouts.doc.tar.xz
Source7687:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cesenaexam.tar.xz
Source7688:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cesenaexam.doc.tar.xz
Source7689:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cheatsheet.tar.xz
Source7690:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cheatsheet.doc.tar.xz
Source7691:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/childdoc.tar.xz
Source7692:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/childdoc.doc.tar.xz
Source8092:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cascade.tar.xz
Source8093:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cascade.doc.tar.xz
Source8094:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cellprops.tar.xz
Source8095:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/cellprops.doc.tar.xz
Source8096:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemsec.tar.xz
Source8097:     http://ftp.math.utah.edu/pub/tex/historic/systems/texlive/2018/tlnet-final/archive/chemsec.doc.tar.xz

%description
The TeX Live software distribution offers a complete TeX system for a
variety of Unix, Macintosh, Windows and other platforms. It
encompasses programs for editing, typesetting, previewing and printing
of TeX documents in many different languages, and a large collection
of TeX macros and font libraries.

The distribution includes extensive general documentation about TeX,
as well as the documentation for the included software packages.


%package -n texlive-blacklettert1
Provides:       tex-blacklettert1 = %{tl_version}
License:        LPPL
Summary:        T1-encoded versions of Haralambous old German fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tfrak.tfm) = %{tl_version}, tex(tfrakls.tfm) = %{tl_version}
Provides:       tex(tgoth.tfm) = %{tl_version}, tex(tswab.tfm) = %{tl_version}
Provides:       tex(tfrak.vf) = %{tl_version}, tex(tfrakls.vf) = %{tl_version}
Provides:       tex(tgoth.vf) = %{tl_version}, tex(tswab.vf) = %{tl_version}
Provides:       tex(t1yfrak.fd) = %{tl_version}

%description -n texlive-blacklettert1
This package contains virtual fonts that offer T1-alike encoded
variants of Yannis Haralambous's old German fonts Gothic,
Schwabacher and Fraktur (which are also available in Adobe type
1 format). The package includes LaTeX macros to embed the fonts
into the LaTeX font selection scheme.

%package -n texlive-blacklettert1-doc
Summary:        Documentation for blacklettert1
Version:        svn15878.0

Provides:       tex-blacklettert1-doc
AutoReqProv:    No

%description -n texlive-blacklettert1-doc
Documentation for blacklettert1

%package -n texlive-blindtext
Provides:       tex-blindtext = %{tl_version}
License:        LPPL
Summary:        Producing 'blind' text for testing
Version:        svn25039.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty)
Provides:       tex(blindtext.sty) = %{tl_version}

%description -n texlive-blindtext
The package provides the commands \blindtext and \Blindtext for
creating 'blind' text useful in testing new classes and
packages, and \blinddocument, \Blinddocument for creating an
entire random document with sections, lists, mathematics, etc.
The package supports three languages, english, (n)german and
latin; the latin option provides a short "lorem ipsum" (for a
fuller lorem ipsum text, see the lipsum package).

%package -n texlive-blindtext-doc
Summary:        Documentation for blindtext
Version:        svn25039.2.0

Provides:       tex-blindtext-doc
AutoReqProv:    No

%description -n texlive-blindtext-doc
Documentation for blindtext

%package -n texlive-blkarray
Provides:       tex-blkarray = %{tl_version}
License:        LPPL
Summary:        Extended array and tabular
Version:        svn36406.0.07

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(blkarray.sty) = %{tl_version}

%description -n texlive-blkarray
An experimental package which implements an environment,
blockarray, that may be used in the same way as the array or
tabular environments of standard LaTeX, or their extended
versions defined in array. If used in math-mode, blockarray
acts like array, otherwise it acts like tabular. The package
implements a new method of defining column types, and also
block and block* environments, for specifying sub-arrays of the
main array. What's more, the \footnote command works inside a
blockarray.

%package -n texlive-blkarray-doc
Summary:        Documentation for blkarray
Version:        svn36406.0.07

Provides:       tex-blkarray-doc
AutoReqProv:    No

%description -n texlive-blkarray-doc
Documentation for blkarray

%package -n texlive-blochsphere
Provides:       tex-blochsphere = %{tl_version}
License:        LPPL 1.3
Summary:        Draw pseudo-3D diagrams of Bloch spheres
Version:        svn38388

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(blochsphere.sty) = %{tl_version}

%description -n texlive-blochsphere
This package is used to draw pseudo-3D Blochsphere diagrams. It
supports various annotations, such as great and small circles,
axes, rotation markings and state vectors. It can be used in a
standalone fashion, or nested within a tikzpicture environment
by setting the environment option nested to true.

%package -n texlive-blochsphere-doc
Summary:        Documentation for blochsphere
Version:        svn38388

Provides:       tex-blochsphere-doc
AutoReqProv:    No

%description -n texlive-blochsphere-doc
Documentation for blochsphere

%package -n texlive-blockdraw_mp
Provides:       tex-blockdraw_mp = %{tl_version}
License:        LPPL
Summary:        Block diagrams and bond graphs, with MetaPost
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-blockdraw_mp
A set of simple MetaPost macros for the task. While the task is
not itself difficult to program, it is felt that many users
will be happy to have a library for the job..

%package -n texlive-blockdraw_mp-doc
Summary:        Documentation for blockdraw_mp
Version:        svn15878.0

Provides:       tex-blockdraw_mp-doc
AutoReqProv:    No

%description -n texlive-blockdraw_mp-doc
Documentation for blockdraw_mp

%package -n texlive-block
Provides:       tex-block = %{tl_version}
License:        Public Domain
Summary:        A block letter style for the letter class
Version:        svn17209.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(block.sty) = %{tl_version}

%description -n texlive-block
A style file for use with the letter class that overwrites the
\opening and \closing macros so that letters can be styled with
the block letter style instead of the default style. Thus, the
return address, the closing, and the signature appear flushed
on the left margin.

%package -n texlive-block-doc
Summary:        Documentation for block
Version:        svn17209.0

Provides:       tex-block-doc
AutoReqProv:    No

%description -n texlive-block-doc
Documentation for block

%package -n texlive-bloques
Provides:       tex-bloques = %{tl_version}
License:        LPPL 1.3
Summary:        Generate control diagrams
Version:        svn22490.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bloques.sty) = %{tl_version}

%description -n texlive-bloques
The package uses TikZ to provide commands for generating
control diagrams (specially in power electronics).

%package -n texlive-bloques-doc
Summary:        Documentation for bloques
Version:        svn22490.1.0

Provides:       tex-bloques-doc
AutoReqProv:    No

%description -n texlive-bloques-doc
Documentation for bloques

%if 0

%package -n texlive-blowup
Provides:       tex-blowup = %{tl_version}
License:        LPPL
Summary:        Upscale or downscale all pages of a document
Version:        svn15878.0.1j

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(everyshi.sty), tex(graphics.sty), tex(keyval.sty), tex(typearea.sty)
Provides:       tex(blowup.sty) = %{tl_version}

%description -n texlive-blowup
The package blowup only defines the user-level macro \blowup,
which can be used to upscale or downscale all pages of a
document. It is similar to the TeX primitive \magnification but
more accurate and user-friendly.

%package -n texlive-blowup-doc
Summary:        Documentation for blowup
Version:        svn15878.0.1j

Provides:       tex-blowup-doc
AutoReqProv:    No

%description -n texlive-blowup-doc
Documentation for blowup

%endif

%package -n texlive-blox
Provides:       tex-blox = %{tl_version}
License:        LPPL
Summary:        Draw block diagrams, using TikZ
Version:        svn35014.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(tikz.sty), tex(pgffor.sty)
Provides:       tex(blox.sty) = %{tl_version}

%description -n texlive-blox
This package, along with TikZ, will typeset block diagrams for
use with programming and control theory. It is an English
translation of the schemabloc package.

%package -n texlive-blox-doc
Summary:        Documentation for blox
Version:        svn35014.2.5

Provides:       tex-blox-doc
AutoReqProv:    No

%description -n texlive-blox-doc
Documentation for blox

%package -n texlive-bnumexpr
Provides:       tex-bnumexpr = %{tl_version}
License:        LPPL 1.3
Summary:        Extends eTeX's \numexpr...\relax construct to big integers
Version:        svn46002
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xintcore.sty), tex(bigintcalc.sty)
Provides:       tex(bnumexpr.sty) = %{tl_version}

%description -n texlive-bnumexpr
The package extends eTeX \numexpr...\relax operation to allow
big integers. Package option allowpower furthermore enables ^
for power operations. By default, bnumexpr loads package
xintcore (part of the xint bundle) and uses its arithmetic
macros.

%package -n texlive-bnumexpr-doc
Summary:        Documentation for bnumexpr
Version:        svn46002
Provides:       tex-bnumexpr-doc
AutoReqProv:    No

%description -n texlive-bnumexpr-doc
Documentation for bnumexpr

%package -n texlive-bodegraph
Provides:       tex-bodegraph = %{tl_version}
License:        LPPL
Summary:        Draw Bode, Nyquist and Black plots with gnuplot and TikZ
Version:        svn20047.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty), tex(ifsym.sty)
Provides:       tex(bodegraph.sty) = %{tl_version}

%description -n texlive-bodegraph
The package provides facilities to draw Bode, Nyquist and Black
plots using Gnuplot and Tikz. Elementary Transfer Functions and
basic correctors are preprogrammed for use.

%package -n texlive-bodegraph-doc
Summary:        Documentation for bodegraph
Version:        svn20047.1.4

Provides:       tex-bodegraph-doc
AutoReqProv:    No

%description -n texlive-bodegraph-doc
Documentation for bodegraph

%package -n texlive-bohr
Provides:       tex-bohr = %{tl_version}
License:        LPPL 1.3
Summary:        Simple atom representation according to the Bohr model
Version:        svn37657.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(pgfopts.sty), tex(elements.sty)
Provides:       tex(bohr.sty) = %{tl_version}

%description -n texlive-bohr
The package provides means for the creation of simple Bohr
models of atoms up to the atomic number 112. In addition,
commands are provided to convert atomic numbers to element
symbols or element names and vice versa.

%package -n texlive-bohr-doc
Summary:        Documentation for bohr
Version:        svn37657.1.0

Provides:       tex-bohr-doc
AutoReqProv:    No

%description -n texlive-bohr-doc
Documentation for bohr

%package -n texlive-boisik
Provides:       tex-boisik = %{tl_version}
License:        GPLv2+
Summary:        A font inspired by Baskerville design
Version:        svn15878.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bskarr10.tfm) = %{tl_version}, tex(bskex10.tfm) = %{tl_version}
Provides:       tex(bskhc10.tfm) = %{tl_version}, tex(bski10-TS1.tfm) = %{tl_version}
Provides:       tex(bski10.tfm) = %{tl_version}, tex(bskib10.tfm) = %{tl_version}
Provides:       tex(bskiol10.tfm) = %{tl_version}, tex(bskiu10.tfm) = %{tl_version}
Provides:       tex(bskiub10.tfm) = %{tl_version}, tex(bskma10.tfm) = %{tl_version}
Provides:       tex(bskmab10.tfm) = %{tl_version}, tex(bskmi10.tfm) = %{tl_version}
Provides:       tex(bskmib10.tfm) = %{tl_version}, tex(bskms10.tfm) = %{tl_version}
Provides:       tex(bskmsb10.tfm) = %{tl_version}, tex(bskmsbsl10.tfm) = %{tl_version}
Provides:       tex(bskmssl10.tfm) = %{tl_version}, tex(bskr10-T1.tfm) = %{tl_version}
Provides:       tex(bskr10-TS1.tfm) = %{tl_version}, tex(bskr10.tfm) = %{tl_version}
Provides:       tex(bskrb10.tfm) = %{tl_version}, tex(bskrc10.tfm) = %{tl_version}
Provides:       tex(bskrcb10.tfm) = %{tl_version}, tex(bskrf10.tfm) = %{tl_version}
Provides:       tex(bskrl10.tfm) = %{tl_version}, tex(bskrol10.tfm) = %{tl_version}
Provides:       tex(bskrsb10.tfm) = %{tl_version}, tex(bskrsl10.tfm) = %{tl_version}
Provides:       tex(bskrw10.tfm) = %{tl_version}, tex(bsksc10.tfm) = %{tl_version}
Provides:       tex(bsksy10.tfm) = %{tl_version}, tex(bsksyol10.tfm) = %{tl_version}
Provides:       tex(bsksysl10.tfm) = %{tl_version}, tex(boisik.sty) = %{tl_version}
Provides:       tex(il2bsk.fd) = %{tl_version}, tex(il2bskf.fd) = %{tl_version}
Provides:       tex(lblbskm.fd) = %{tl_version}, tex(lblcmr.fd) = %{tl_version}
Provides:       tex(lblenc.def) = %{tl_version}, tex(lbmbsk.fd) = %{tl_version}
Provides:       tex(lbmbskms.fd) = %{tl_version}, tex(lbmcmr.fd) = %{tl_version}
Provides:       tex(lbmenc.def) = %{tl_version}, tex(lbsbsk.fd) = %{tl_version}
Provides:       tex(lbsbsksy.fd) = %{tl_version}, tex(lbscmr.fd) = %{tl_version}
Provides:       tex(lbsenc.def) = %{tl_version}, tex(ot1bsk.fd) = %{tl_version}
Provides:       tex(ot1bskf.fd) = %{tl_version}, tex(ts1bsk.fd) = %{tl_version}
Provides:       tex(ubskex.fd) = %{tl_version}

%description -n texlive-boisik
Boisik is a serif font set (inspired by the Baskerville
typeface), written in Metafont. The set comprises roman and
italic text fonts and maths fonts. LaTeX support is offered for
use with OT1, IL2 and OM* encodings.

%package -n texlive-boisik-doc
Summary:        Documentation for boisik
Version:        svn15878.0.5

Provides:       tex-boisik-doc
AutoReqProv:    No

%description -n texlive-boisik-doc
Documentation for boisik

%package -n texlive-boites
Provides:       tex-boites = %{tl_version}
License:        GPL+
Summary:        Boxes that may break across pages
Version:        svn32235.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(boites.sty) = %{tl_version}, tex(boites_exemples.sty) = %{tl_version}

%description -n texlive-boites
Defines environments that allow page breaks inside framed boxes
whose edges may be variously fancy. The bundle includes a few
examples (shaded box, box with a wavy line on its side, etc).

%package -n texlive-boites-doc
Summary:        Documentation for boites
Version:        svn32235.1.1

Provides:       tex-boites-doc
AutoReqProv:    No

%description -n texlive-boites-doc
Documentation for boites

%package -n texlive-bold-extra
Provides:       tex-bold-extra = %{tl_version}
License:        LPPL
Summary:        Use bold small caps and typewriter fonts
Version:        svn17076.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bold-extra.sty) = %{tl_version}

%description -n texlive-bold-extra
Allows access to 'extra' bold fonts for Computer Modern OT1
encoding (the fonts are available in Metafont source). Since
there is more than one bold tt-family font set, the version
required is selected by a package option.

%package -n texlive-bold-extra-doc
Summary:        Documentation for bold-extra
Version:        svn17076.0.1

Provides:       tex-bold-extra-doc
AutoReqProv:    No

%description -n texlive-bold-extra-doc
Documentation for bold-extra

%package -n texlive-boldtensors
Provides:       tex-boldtensors = %{tl_version}
License:        GPL+
Summary:        Bold latin and greek characters through simple prefix characters
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(boldtensors.sty) = %{tl_version}

%description -n texlive-boldtensors
This package provides bold latin and greek characters within
\mathversion{normal}, by using ~ and " as prefix characters.

%package -n texlive-boldtensors-doc
Summary:        Documentation for boldtensors
Version:        svn15878.0

Provides:       tex-boldtensors-doc
AutoReqProv:    No

%description -n texlive-boldtensors-doc
Documentation for boldtensors

%package -n texlive-bondgraphs
Provides:       tex-bondgraphs = %{tl_version}
License:        LPPL 1.3
Summary:        Draws bond graphs in LaTeX, using pgf/TikZ
Version:        svn36605.1.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(amsfonts.sty), tex(bm.sty), tex(kvoptions.sty)
Provides:       tex(bondgraphs.sty) = %{tl_version}

%description -n texlive-bondgraphs
The package is used to draw bond graphs in LaTeX. It uses a
recent version (3.0+) of PGF and TikZ for the drawing, hence,
it is mainly a set of TikZ styles that makes the drawing of
bond graphs easier. Compared to the bondgraph package this
package relies more on TikZ styles and less on macros, to
generate the drawings. As such it can be more flexible than
his, but requires more TikZ knowledge of the user.

%package -n texlive-bondgraphs-doc
Summary:        Documentation for bondgraphs
Version:        svn36605.1.0.1

Provides:       tex-bondgraphs-doc
AutoReqProv:    No

%description -n texlive-bondgraphs-doc
Documentation for bondgraphs

%package -n texlive-bondgraph
Provides:       tex-bondgraph = %{tl_version}
License:        LPPL 1.3
Summary:        Create bond graph figures in LaTeX documents
Version:        svn21670.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty), tex(ifthen.sty)
Provides:       tex(bondgraph.sty) = %{tl_version}

%description -n texlive-bondgraph
The package draws bond graphs using PGF and TikZ.

%package -n texlive-bondgraph-doc
Summary:        Documentation for bondgraph
Version:        svn21670.1.0

Provides:       tex-bondgraph-doc
AutoReqProv:    No

%description -n texlive-bondgraph-doc
Documentation for bondgraph

%package -n texlive-bookcover
Provides:       tex-bookcover = %{tl_version}
License:        LPPL 1.2
Summary:        A class for book covers and dust jackets
Version:        svn46410
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty), tex(geometry.sty), tex(graphicx.sty), tex(calc.sty)
Requires:       tex(xcolor.sty), tex(ifthen.sty), tex(tikz.sty), tex(eso-pic.sty)
Requires:       tex(textpos.sty)
Provides:       tex(bookcover.cls) = %{tl_version}

%description -n texlive-bookcover
This class helps typesetting book covers and dust jackets.

%package -n texlive-bookcover-doc
Summary:        Documentation for bookcover
Version:        svn46410
Provides:       tex-bookcover-doc
AutoReqProv:    No

%description -n texlive-bookcover-doc
Documentation for bookcover

%package -n texlive-bookdb
Provides:       tex-bookdb = %{tl_version}
License:        LPPL 1.3
Summary:        A BibTeX style file for cataloguing a home library
Version:        svn37536.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-bookdb
This package provides an extended book entry for use in
cataloguing a home library. The extensions include fields for
binding, category, collator, condition, copy, illustrations,
introduction, location, pages, size, value, volumes.

%package -n texlive-bookdb-doc
Summary:        Documentation for bookdb
Version:        svn37536.0.2

Provides:       tex-bookdb-doc
AutoReqProv:    No

%description -n texlive-bookdb-doc
Documentation for bookdb

%package -n texlive-bookest
Provides:       tex-bookest = %{tl_version}
License:        LPPL
Summary:        Extended book class
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty), tex(setspace.sty), tex(graphicx.sty), tex(hyperref.sty)
Requires:       tex(eso-pic.sty), tex(geometry.sty), tex(everyshi.sty)
Provides:       tex(bookest.cls) = %{tl_version}

%description -n texlive-bookest
The class extends the standard book class, in the areas of
colour scheme management, document layout, headings and
footers, front page layout, and other minor items.

%package -n texlive-bookest-doc
Summary:        Documentation for bookest
Version:        svn15878.1.1

Provides:       tex-bookest-doc
AutoReqProv:    No

%description -n texlive-bookest-doc
Documentation for bookest

%package -n texlive-bookhands
Provides:       tex-bookhands = %{tl_version}
License:        LPPL
Summary:        A collection of book-hand fonts
Version:        svn46480
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(egothic.sty)
Requires:       tex(huncial.sty), tex(inslrmin.sty), tex(rotunda.sty), tex(sqrcaps.sty)
Provides:       tex(sqrcaps.map) = %{tl_version}, tex(auncl17.tfm) = %{tl_version}
Provides:       tex(auncl7.tfm) = %{tl_version}, tex(aunclb17.tfm) = %{tl_version}
Provides:       tex(aunclb7.tfm) = %{tl_version}, tex(cmin10.tfm) = %{tl_version}
Provides:       tex(cmin17.tfm) = %{tl_version}, tex(cmin7.tfm) = %{tl_version}
Provides:       tex(cminb10.tfm) = %{tl_version}, tex(cminb17.tfm) = %{tl_version}
Provides:       tex(cminb7.tfm) = %{tl_version}, tex(egoth10.tfm) = %{tl_version}
Provides:       tex(egoth17.tfm) = %{tl_version}, tex(egoth7.tfm) = %{tl_version}
Provides:       tex(egothb10.tfm) = %{tl_version}, tex(egothb17.tfm) = %{tl_version}
Provides:       tex(egothb7.tfm) = %{tl_version}, tex(hmin10.tfm) = %{tl_version}
Provides:       tex(hmin17.tfm) = %{tl_version}, tex(hmin7.tfm) = %{tl_version}
Provides:       tex(hminb10.tfm) = %{tl_version}, tex(hminb17.tfm) = %{tl_version}
Provides:       tex(hminb7.tfm) = %{tl_version}, tex(huncl10.tfm) = %{tl_version}
Provides:       tex(huncl17.tfm) = %{tl_version}, tex(huncl7.tfm) = %{tl_version}
Provides:       tex(hunclb10.tfm) = %{tl_version}, tex(hunclb17.tfm) = %{tl_version}
Provides:       tex(hunclb7.tfm) = %{tl_version}, tex(imaj10.tfm) = %{tl_version}
Provides:       tex(imaj17.tfm) = %{tl_version}, tex(imaj7.tfm) = %{tl_version}
Provides:       tex(imajb10.tfm) = %{tl_version}, tex(imajb17.tfm) = %{tl_version}
Provides:       tex(imajb7.tfm) = %{tl_version}, tex(imin10.tfm) = %{tl_version}
Provides:       tex(imin17.tfm) = %{tl_version}, tex(imin7.tfm) = %{tl_version}
Provides:       tex(iminb10.tfm) = %{tl_version}, tex(iminb17.tfm) = %{tl_version}
Provides:       tex(iminb7.tfm) = %{tl_version}, tex(pgoth10.tfm) = %{tl_version}
Provides:       tex(pgoth17.tfm) = %{tl_version}, tex(pgoth7.tfm) = %{tl_version}
Provides:       tex(pgothb10.tfm) = %{tl_version}, tex(pgothb17.tfm) = %{tl_version}
Provides:       tex(rtnd10.tfm) = %{tl_version}, tex(rtnd17.tfm) = %{tl_version}
Provides:       tex(rtnd7.tfm) = %{tl_version}, tex(rtndb10.tfm) = %{tl_version}
Provides:       tex(rtndb17.tfm) = %{tl_version}, tex(rtndb7.tfm) = %{tl_version}
Provides:       tex(rust10.tfm) = %{tl_version}, tex(rust17.tfm) = %{tl_version}
Provides:       tex(rust7.tfm) = %{tl_version}, tex(rustb10.tfm) = %{tl_version}
Provides:       tex(rustb17.tfm) = %{tl_version}, tex(rustb7.tfm) = %{tl_version}
Provides:       tex(sqrc10.tfm) = %{tl_version}, tex(sqrcb10.tfm) = %{tl_version}
Provides:       tex(uncl10.tfm) = %{tl_version}, tex(uncl17.tfm) = %{tl_version}
Provides:       tex(uncl7.tfm) = %{tl_version}, tex(unclb10.tfm) = %{tl_version}
Provides:       tex(unclb17.tfm) = %{tl_version}, tex(unclb7.tfm) = %{tl_version}
Provides:       tex(sqrc10.pfb) = %{tl_version}, tex(sqrcb10.pfb) = %{tl_version}
Provides:       tex(allcmin.sty) = %{tl_version}, tex(allegoth.sty) = %{tl_version}
Provides:       tex(allhmin.sty) = %{tl_version}, tex(allhuncl.sty) = %{tl_version}
Provides:       tex(allimaj.sty) = %{tl_version}, tex(allimin.sty) = %{tl_version}
Provides:       tex(allpgoth.sty) = %{tl_version}, tex(allrtnd.sty) = %{tl_version}
Provides:       tex(allrust.sty) = %{tl_version}, tex(allsqrc.sty) = %{tl_version}
Provides:       tex(alluncl.sty) = %{tl_version}, tex(carolmin.sty) = %{tl_version}
Provides:       tex(egothic.sty) = %{tl_version}, tex(humanist.sty) = %{tl_version}
Provides:       tex(huncial.sty) = %{tl_version}, tex(inslrmaj.sty) = %{tl_version}
Provides:       tex(inslrmin.sty) = %{tl_version}, tex(ot1auncl.fd) = %{tl_version}
Provides:       tex(ot1cmin.fd) = %{tl_version}, tex(ot1egoth.fd) = %{tl_version}
Provides:       tex(ot1hmin.fd) = %{tl_version}, tex(ot1huncl.fd) = %{tl_version}
Provides:       tex(ot1imaj.fd) = %{tl_version}, tex(ot1imin.fd) = %{tl_version}
Provides:       tex(ot1pgoth.fd) = %{tl_version}, tex(ot1rtnd.fd) = %{tl_version}
Provides:       tex(ot1rust.fd) = %{tl_version}, tex(ot1sqrc.fd) = %{tl_version}
Provides:       tex(ot1uncl.fd) = %{tl_version}, tex(pgothic.sty) = %{tl_version}
Provides:       tex(rotunda.sty) = %{tl_version}, tex(rustic.sty) = %{tl_version}
Provides:       tex(sqrcaps.sty) = %{tl_version}, tex(t1auncl.fd) = %{tl_version}
Provides:       tex(t1cmin.fd) = %{tl_version}, tex(t1egoth.fd) = %{tl_version}
Provides:       tex(t1hmin.fd) = %{tl_version}, tex(t1huncl.fd) = %{tl_version}
Provides:       tex(t1imaj.fd) = %{tl_version}, tex(t1imin.fd) = %{tl_version}
Provides:       tex(t1pgoth.fd) = %{tl_version}, tex(t1rtnd.fd) = %{tl_version}
Provides:       tex(t1rust.fd) = %{tl_version}, tex(t1sqrc.fd) = %{tl_version}
Provides:       tex(t1uncl.fd) = %{tl_version}, tex(uncial.sty) = %{tl_version}

%description -n texlive-bookhands
This is a set of book-hand (MetaFont) fonts and packages
covering manuscript scripts from the 1st century until
Gutenberg and Caxton. The included hands are: Square Capitals
(1st century onwards); Roman Rustic (1st-6th centuries);
Insular Minuscule (6th cenury onwards); Carolingian Minuscule
(8th-12th centuries); Early Gothic (11th-12th centuries);
Gothic Textura Quadrata (13th-15th centuries); Gothic Textura
Prescisus vel sine pedibus (13th century onwards); Rotunda (13-
15th centuries); Humanist Minuscule (14th century onwards);
Uncial (3rd-6th centuries); Half Uncial (3rd-9th centuries);
Artificial Uncial (6th-10th centuries); and Insular Majuscule
(6th-9th centuries).

%package -n texlive-bookhands-doc
Summary:        Documentation for bookhands
Version:        svn46480
Provides:       tex-bookhands-doc
AutoReqProv:    No

%description -n texlive-bookhands-doc
Documentation for bookhands

%package -n texlive-booklet
Provides:       tex-booklet = %{tl_version}
License:        LPPL 1.3
Summary:        Aids for printing simple booklets
Version:        svn15878.0.7b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bkltprnt.sty) = %{tl_version}, tex(booklet.sty) = %{tl_version}

%description -n texlive-booklet
Pages of a document processed with the booklet package will be
reordered and scaled so that they can be printed as four pages
per physical sheet of paper, two pages per side. The resulting
sheets will, when folded in half, assemble into a booklet.
Instructions on producing the manual itself as a booklet are
included.

%package -n texlive-booklet-doc
Summary:        Documentation for booklet
Version:        svn15878.0.7b

Provides:       tex-booklet-doc
AutoReqProv:    No

%description -n texlive-booklet-doc
Documentation for booklet

%package -n texlive-bookman
Provides:       tex-bookman = %{tl_version}
License:        GPL+
Summary:        URW "Base 35" font pack for LaTeX
Version:        svn31835.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ubk.map) = %{tl_version}, tex(pbkd.tfm) = %{tl_version}
Provides:       tex(pbkd7t.tfm) = %{tl_version}, tex(pbkd8c.tfm) = %{tl_version}
Provides:       tex(pbkd8r.tfm) = %{tl_version}, tex(pbkd8t.tfm) = %{tl_version}
Provides:       tex(pbkdc.tfm) = %{tl_version}, tex(pbkdc7t.tfm) = %{tl_version}
Provides:       tex(pbkdc8t.tfm) = %{tl_version}, tex(pbkdi.tfm) = %{tl_version}
Provides:       tex(pbkdi7t.tfm) = %{tl_version}, tex(pbkdi8c.tfm) = %{tl_version}
Provides:       tex(pbkdi8r.tfm) = %{tl_version}, tex(pbkdi8t.tfm) = %{tl_version}
Provides:       tex(pbkdo.tfm) = %{tl_version}, tex(pbkdo7t.tfm) = %{tl_version}
Provides:       tex(pbkdo8c.tfm) = %{tl_version}, tex(pbkdo8r.tfm) = %{tl_version}
Provides:       tex(pbkdo8t.tfm) = %{tl_version}, tex(pbkl.tfm) = %{tl_version}
Provides:       tex(pbkl7t.tfm) = %{tl_version}, tex(pbkl8c.tfm) = %{tl_version}
Provides:       tex(pbkl8r.tfm) = %{tl_version}, tex(pbkl8t.tfm) = %{tl_version}
Provides:       tex(pbklc.tfm) = %{tl_version}, tex(pbklc7t.tfm) = %{tl_version}
Provides:       tex(pbklc8t.tfm) = %{tl_version}, tex(pbkli.tfm) = %{tl_version}
Provides:       tex(pbkli7t.tfm) = %{tl_version}, tex(pbkli8c.tfm) = %{tl_version}
Provides:       tex(pbkli8r.tfm) = %{tl_version}, tex(pbkli8t.tfm) = %{tl_version}
Provides:       tex(pbklo.tfm) = %{tl_version}, tex(pbklo7t.tfm) = %{tl_version}
Provides:       tex(pbklo8c.tfm) = %{tl_version}, tex(pbklo8r.tfm) = %{tl_version}
Provides:       tex(pbklo8t.tfm) = %{tl_version}, tex(ubkb7t.tfm) = %{tl_version}
Provides:       tex(ubkb8c.tfm) = %{tl_version}, tex(ubkb8r.tfm) = %{tl_version}
Provides:       tex(ubkb8t.tfm) = %{tl_version}, tex(ubkbc7t.tfm) = %{tl_version}
Provides:       tex(ubkbc8t.tfm) = %{tl_version}, tex(ubkbi7t.tfm) = %{tl_version}
Provides:       tex(ubkbi8c.tfm) = %{tl_version}, tex(ubkbi8r.tfm) = %{tl_version}
Provides:       tex(ubkbi8t.tfm) = %{tl_version}, tex(ubkbo7t.tfm) = %{tl_version}
Provides:       tex(ubkbo8c.tfm) = %{tl_version}, tex(ubkbo8r.tfm) = %{tl_version}
Provides:       tex(ubkbo8t.tfm) = %{tl_version}, tex(ubkd7t.tfm) = %{tl_version}
Provides:       tex(ubkd8c.tfm) = %{tl_version}, tex(ubkd8r.tfm) = %{tl_version}
Provides:       tex(ubkd8t.tfm) = %{tl_version}, tex(ubkdc7t.tfm) = %{tl_version}
Provides:       tex(ubkdc8t.tfm) = %{tl_version}, tex(ubkdi7t.tfm) = %{tl_version}
Provides:       tex(ubkdi8c.tfm) = %{tl_version}, tex(ubkdi8r.tfm) = %{tl_version}
Provides:       tex(ubkdi8t.tfm) = %{tl_version}, tex(ubkdo7t.tfm) = %{tl_version}
Provides:       tex(ubkdo8c.tfm) = %{tl_version}, tex(ubkdo8r.tfm) = %{tl_version}
Provides:       tex(ubkdo8t.tfm) = %{tl_version}, tex(ubkl7t.tfm) = %{tl_version}
Provides:       tex(ubkl8c.tfm) = %{tl_version}, tex(ubkl8r.tfm) = %{tl_version}
Provides:       tex(ubkl8t.tfm) = %{tl_version}, tex(ubklc7t.tfm) = %{tl_version}
Provides:       tex(ubklc8t.tfm) = %{tl_version}, tex(ubkli7t.tfm) = %{tl_version}
Provides:       tex(ubkli8c.tfm) = %{tl_version}, tex(ubkli8r.tfm) = %{tl_version}
Provides:       tex(ubkli8t.tfm) = %{tl_version}, tex(ubklo7t.tfm) = %{tl_version}
Provides:       tex(ubklo8c.tfm) = %{tl_version}, tex(ubklo8r.tfm) = %{tl_version}
Provides:       tex(ubklo8t.tfm) = %{tl_version}, tex(ubkr7t.tfm) = %{tl_version}
Provides:       tex(ubkr8c.tfm) = %{tl_version}, tex(ubkr8r.tfm) = %{tl_version}
Provides:       tex(ubkr8t.tfm) = %{tl_version}, tex(ubkrc7t.tfm) = %{tl_version}
Provides:       tex(ubkrc8t.tfm) = %{tl_version}, tex(ubkri7t.tfm) = %{tl_version}
Provides:       tex(ubkri8c.tfm) = %{tl_version}, tex(ubkri8r.tfm) = %{tl_version}
Provides:       tex(ubkri8t.tfm) = %{tl_version}, tex(ubkro7t.tfm) = %{tl_version}
Provides:       tex(ubkro8c.tfm) = %{tl_version}, tex(ubkro8r.tfm) = %{tl_version}
Provides:       tex(ubkro8t.tfm) = %{tl_version}, tex(ubkd8a.pfb) = %{tl_version}
Provides:       tex(ubkdi8a.pfb) = %{tl_version}, tex(ubkl8a.pfb) = %{tl_version}
Provides:       tex(ubkli8a.pfb) = %{tl_version}, tex(pbkd.vf) = %{tl_version}
Provides:       tex(pbkd7t.vf) = %{tl_version}, tex(pbkd8c.vf) = %{tl_version}
Provides:       tex(pbkd8t.vf) = %{tl_version}, tex(pbkdc.vf) = %{tl_version}
Provides:       tex(pbkdc7t.vf) = %{tl_version}, tex(pbkdc8t.vf) = %{tl_version}
Provides:       tex(pbkdi.vf) = %{tl_version}, tex(pbkdi7t.vf) = %{tl_version}
Provides:       tex(pbkdi8c.vf) = %{tl_version}, tex(pbkdi8t.vf) = %{tl_version}
Provides:       tex(pbkdo.vf) = %{tl_version}, tex(pbkdo7t.vf) = %{tl_version}
Provides:       tex(pbkdo8c.vf) = %{tl_version}, tex(pbkdo8t.vf) = %{tl_version}
Provides:       tex(pbkl.vf) = %{tl_version}, tex(pbkl7t.vf) = %{tl_version}
Provides:       tex(pbkl8c.vf) = %{tl_version}, tex(pbkl8t.vf) = %{tl_version}
Provides:       tex(pbklc.vf) = %{tl_version}, tex(pbklc7t.vf) = %{tl_version}
Provides:       tex(pbklc8t.vf) = %{tl_version}, tex(pbkli.vf) = %{tl_version}
Provides:       tex(pbkli7t.vf) = %{tl_version}, tex(pbkli8c.vf) = %{tl_version}
Provides:       tex(pbkli8t.vf) = %{tl_version}, tex(pbklo.vf) = %{tl_version}
Provides:       tex(pbklo7t.vf) = %{tl_version}, tex(pbklo8c.vf) = %{tl_version}
Provides:       tex(pbklo8t.vf) = %{tl_version}, tex(ubkb7t.vf) = %{tl_version}
Provides:       tex(ubkb8c.vf) = %{tl_version}, tex(ubkb8t.vf) = %{tl_version}
Provides:       tex(ubkbc7t.vf) = %{tl_version}, tex(ubkbc8t.vf) = %{tl_version}
Provides:       tex(ubkbi7t.vf) = %{tl_version}, tex(ubkbi8c.vf) = %{tl_version}
Provides:       tex(ubkbi8t.vf) = %{tl_version}, tex(ubkbo7t.vf) = %{tl_version}
Provides:       tex(ubkbo8c.vf) = %{tl_version}, tex(ubkbo8t.vf) = %{tl_version}
Provides:       tex(ubkd7t.vf) = %{tl_version}, tex(ubkd8c.vf) = %{tl_version}
Provides:       tex(ubkd8t.vf) = %{tl_version}, tex(ubkdc7t.vf) = %{tl_version}
Provides:       tex(ubkdc8t.vf) = %{tl_version}, tex(ubkdi7t.vf) = %{tl_version}
Provides:       tex(ubkdi8c.vf) = %{tl_version}, tex(ubkdi8t.vf) = %{tl_version}
Provides:       tex(ubkdo7t.vf) = %{tl_version}, tex(ubkdo8c.vf) = %{tl_version}
Provides:       tex(ubkdo8t.vf) = %{tl_version}, tex(ubkl7t.vf) = %{tl_version}
Provides:       tex(ubkl8c.vf) = %{tl_version}, tex(ubkl8t.vf) = %{tl_version}
Provides:       tex(ubklc7t.vf) = %{tl_version}, tex(ubklc8t.vf) = %{tl_version}
Provides:       tex(ubkli7t.vf) = %{tl_version}, tex(ubkli8c.vf) = %{tl_version}
Provides:       tex(ubkli8t.vf) = %{tl_version}, tex(ubklo7t.vf) = %{tl_version}
Provides:       tex(ubklo8c.vf) = %{tl_version}, tex(ubklo8t.vf) = %{tl_version}
Provides:       tex(ubkr7t.vf) = %{tl_version}, tex(ubkr8c.vf) = %{tl_version}
Provides:       tex(ubkr8t.vf) = %{tl_version}, tex(ubkrc7t.vf) = %{tl_version}
Provides:       tex(ubkrc8t.vf) = %{tl_version}, tex(ubkri7t.vf) = %{tl_version}
Provides:       tex(ubkri8c.vf) = %{tl_version}, tex(ubkri8t.vf) = %{tl_version}
Provides:       tex(ubkro7t.vf) = %{tl_version}, tex(ubkro8c.vf) = %{tl_version}
Provides:       tex(ubkro8t.vf) = %{tl_version}, tex(8rubk.fd) = %{tl_version}
Provides:       tex(omlubk.fd) = %{tl_version}, tex(omsubk.fd) = %{tl_version}
Provides:       tex(ot1ubk.fd) = %{tl_version}, tex(t1ubk.fd) = %{tl_version}
Provides:       tex(ts1ubk.fd) = %{tl_version}

%description -n texlive-bookman
A set of fonts for use as "drop-in" replacements for Adobe's
basic set, comprising: Century Schoolbook (substituting for
Adobe's New Century Schoolbook); Dingbats (substituting for
Adobe's Zapf Dingbats); Nimbus Mono L (substituting for Abobe's
Courier); Nimbus Roman No9 L (substituting for Adobe's Times);
Nimbus Sans L (substituting for Adobe's Helvetica); Standard
Symbols L (substituting for Adobe's Symbol); URW Bookman; URW
Chancery L Medium Italic (substituting for Adobe's Zapf
Chancery); URW Gothic L Book (substituting for Adobe's Avant
Garde); and URW Palladio L (substituting for Adobe's Palatino).

%package -n texlive-booktabs-de-doc
Summary:        Documentation for booktabs-de
Version:        svn21907.1.61803

Provides:       tex-booktabs-de-doc
AutoReqProv:    No

%description -n texlive-booktabs-de-doc
Documentation for booktabs-de

%package -n texlive-booktabs-fr-doc
Summary:        Documentation for booktabs-fr
Version:        svn21948.1.00

Provides:       tex-booktabs-fr-doc
AutoReqProv:    No

%description -n texlive-booktabs-fr-doc
Documentation for booktabs-fr

%package -n texlive-booktabs
Provides:       tex-booktabs = %{tl_version}
License:        GPL+
Summary:        Publication quality tables in LaTeX
Version:        svn40846

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(booktabs.sty) = %{tl_version}

%description -n texlive-booktabs
The package enhances the quality of tables in LaTeX, providing
extra commands as well as behind-the-scenes optimisation.
Guidelines are given as to what constitutes a good table in
this context. From version 1.61, the package offers longtable
compatibility.

%package -n texlive-booktabs-doc
Summary:        Documentation for booktabs
Version:        svn40846

Provides:       tex-booktabs-doc
AutoReqProv:    No

%description -n texlive-booktabs-doc
Documentation for booktabs

%package -n texlive-boolexpr
Provides:       tex-boolexpr = %{tl_version}
License:        LPPL
Summary:        A boolean expression evaluator and a switch command
Version:        svn17830.3.14

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(boolexpr.sty) = %{tl_version}

%description -n texlive-boolexpr
The \boolexpr macro evaluates boolean expressions in a purely
expandable way. \boolexpr{ A \OR B \AND C } expands to 0 if the
logical expression is TRUE. A, B, C may be: numeric expressions
such as: x=y, x<>y, x>y or x<y; - boolean switches: \iftrue
0\else 1\fi; - conditionals: \ifcsname whatsit\endcsname 0\else
1\fi; - another \boolexpr: \boolexpr{ D \OR E \AND F }:
\boolexpr may be used with \ifcase: \ifcase\boolexpr{ A \OR B
\AND C } What to do if true \else What to do if false \fi The
\switch command (which is also expandable) has the form:
\switch \case{<boolean expression>} ... \case{<boolean
expression>} ... ... \otherwise ... \endswitch

%package -n texlive-boolexpr-doc
Summary:        Documentation for boolexpr
Version:        svn17830.3.14

Provides:       tex-boolexpr-doc
AutoReqProv:    No

%description -n texlive-boolexpr-doc
Documentation for boolexpr

%package -n texlive-boondox
Provides:       tex-boondox = %{tl_version}
License:        LPPL
Summary:        Mathematical alphabets derived from the STIX fonts
Version:        svn43344
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(xkeyval.sty)
Provides:       tex(boondox.map) = %{tl_version}, tex(BOONDOX-b-cal.tfm) = %{tl_version}
Provides:       tex(BOONDOX-b-calo.tfm) = %{tl_version}, tex(BOONDOX-b-ds.tfm) = %{tl_version}
Provides:       tex(BOONDOX-b-frak.tfm) = %{tl_version}, tex(BOONDOX-r-cal.tfm) = %{tl_version}
Provides:       tex(BOONDOX-r-calo.tfm) = %{tl_version}, tex(BOONDOX-r-ds.tfm) = %{tl_version}
Provides:       tex(BOONDOX-r-frak.tfm) = %{tl_version}, tex(zxxbf7z.tfm) = %{tl_version}
Provides:       tex(zxxbf8a.tfm) = %{tl_version}, tex(zxxbl7z.tfm) = %{tl_version}
Provides:       tex(zxxbl8a.tfm) = %{tl_version}, tex(zxxbow7z.tfm) = %{tl_version}
Provides:       tex(zxxbw7z.tfm) = %{tl_version}, tex(zxxbw8a.tfm) = %{tl_version}
Provides:       tex(zxxrf7z.tfm) = %{tl_version}, tex(zxxrf8a.tfm) = %{tl_version}
Provides:       tex(zxxrl7z.tfm) = %{tl_version}, tex(zxxrl8a.tfm) = %{tl_version}
Provides:       tex(zxxrow7z.tfm) = %{tl_version}, tex(zxxrw7z.tfm) = %{tl_version}
Provides:       tex(zxxrw8a.tfm) = %{tl_version}, tex(zxxbf8a.pfb) = %{tl_version}
Provides:       tex(zxxbl8a.pfb) = %{tl_version}, tex(zxxbw8a.pfb) = %{tl_version}
Provides:       tex(zxxrf8a.pfb) = %{tl_version}, tex(zxxrl8a.pfb) = %{tl_version}
Provides:       tex(zxxrw8a.pfb) = %{tl_version}, tex(BOONDOX-b-cal.vf) = %{tl_version}
Provides:       tex(BOONDOX-b-calo.vf) = %{tl_version}, tex(BOONDOX-b-ds.vf) = %{tl_version}
Provides:       tex(BOONDOX-b-frak.vf) = %{tl_version}, tex(BOONDOX-r-cal.vf) = %{tl_version}
Provides:       tex(BOONDOX-r-calo.vf) = %{tl_version}, tex(BOONDOX-r-ds.vf) = %{tl_version}
Provides:       tex(BOONDOX-r-frak.vf) = %{tl_version}, tex(BOONDOX-cal.sty) = %{tl_version}
Provides:       tex(BOONDOX-calo.sty) = %{tl_version}, tex(BOONDOX-ds.sty) = %{tl_version}
Provides:       tex(BOONDOX-frak.sty) = %{tl_version}, tex(uboondox-cal.fd) = %{tl_version}
Provides:       tex(uboondox-calo.fd) = %{tl_version}, tex(uboondox-ds.fd) = %{tl_version}
Provides:       tex(uboondox-frak.fd) = %{tl_version}

%description -n texlive-boondox
The package contains a number of PostScript fonts derived from
the STIX OpenType fonts, that may be used in maths mode in
regular and bold weights for calligraphic, fraktur and double-
struck alphabets. Virtual fonts with metrics suitable for maths
mode are provided, as are LaTeX support files.

%package -n texlive-boondox-doc
Summary:        Documentation for boondox
Version:        svn43344
Provides:       tex-boondox-doc
AutoReqProv:    No

%description -n texlive-boondox-doc
Documentation for boondox

%package -n texlive-bophook
Provides:       tex-bophook = %{tl_version}
License:        LPPL
Summary:        Provides an At-Begin-Page hook
Version:        svn17062.0.02

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bophook.sty) = %{tl_version}

%description -n texlive-bophook
Using the \AtBeginPage hook, you can add material in the
background of a page. \PageLayout can be used to give page
makeup commands to be executed on every page (e.g., depending
on the page style).

%package -n texlive-bophook-doc
Summary:        Documentation for bophook
Version:        svn17062.0.02

Provides:       tex-bophook-doc
AutoReqProv:    No

%description -n texlive-bophook-doc
Documentation for bophook

%package -n texlive-borceux
Provides:       tex-borceux = %{tl_version}
License:        Borceux
Summary:        Diagram macros by Francois Borceux
Version:        svn21047.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-borceux
The macros support the construction of diagrams, such as those
that appear in category theory texts. The user gives the list
of vertices and arrows to be included, just as when composing a
matrix, and the program takes care of computing the dimensions
of the arrows and realizing the pagesetting. All the user has
to do about the arrows is to specify their type (monomorphism,
pair of adjoint arrows, etc.) and their direction (north, south-
east, etc.); 12 types and 32 directions are available.

%package -n texlive-borceux-doc
Summary:        Documentation for borceux
Version:        svn21047.0

Provides:       tex-borceux-doc
AutoReqProv:    No

%description -n texlive-borceux-doc
Documentation for borceux

%package -n texlive-bosisio
Provides:       tex-bosisio = %{tl_version}
License:        LPPL
Summary:        A collection of packages by Francesco Bosisio
Version:        svn16989.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xspace.sty), tex(graphics.sty), tex(subfigure.sty), tex(float.sty)
Provides:       tex(accenti.sty) = %{tl_version}, tex(dblfont.sty) = %{tl_version}
Provides:       tex(envmath.sty) = %{tl_version}, tex(evenpage.sty) = %{tl_version}
Provides:       tex(graphfig.sty) = %{tl_version}, tex(mathcmd.sty) = %{tl_version}
Provides:       tex(quotes.sty) = %{tl_version}, tex(sobolev.sty) = %{tl_version}

%description -n texlive-bosisio
A collection of packages containing: accenti dblfont; envmath;
evenpage; graphfig; mathcmd; quotes; and sobolev.

%package -n texlive-bosisio-doc
Summary:        Documentation for bosisio
Version:        svn16989.0

Provides:       tex-bosisio-doc
AutoReqProv:    No

%description -n texlive-bosisio-doc
Documentation for bosisio

%package -n texlive-boxedminipage2e
Provides:       tex-boxedminipage2e = %{tl_version}
License:        LPPL 1.3
Summary:        Framed minipages of a specified total width (text and frame combined)
Version:        svn36477.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(boxedminipage2e.sty) = %{tl_version}

%description -n texlive-boxedminipage2e
The package essentially just wraps a minipage within an \fbox.
However, while
\fbox{\begin{minipage}{\linewidth}...\end{minipage}} just out
into the margin, \begin{boxedminipage}...\end{boxedminipage}
does not. Instead, it subtracts the frame's dimensions from the
specified dimensions of the minipage before typesetting the
minipage.

%package -n texlive-boxedminipage2e-doc
Summary:        Documentation for boxedminipage2e
Version:        svn36477.1.0

Provides:       tex-boxedminipage2e-doc
AutoReqProv:    No

%description -n texlive-boxedminipage2e-doc
Documentation for boxedminipage2e

%package -n texlive-boxedminipage
Provides:       tex-boxedminipage = %{tl_version}
License:        Public Domain
Summary:        A package for producing framed minipages
Version:        svn17087.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(boxedminipage.sty) = %{tl_version}

%description -n texlive-boxedminipage
The package defines the boxedminipage environment -- like
minipage, but with a frame around it.

%package -n texlive-boxedminipage-doc
Summary:        Documentation for boxedminipage
Version:        svn17087.2

Provides:       tex-boxedminipage-doc
AutoReqProv:    No

%description -n texlive-boxedminipage-doc
Documentation for boxedminipage

%package -n texlive-boxhandler
Provides:       tex-boxhandler = %{tl_version}
License:        LPPL
Summary:        Flexible Captioning and Deferred Box/List Printing
Version:        svn28031.1.30

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(boxhandler.sty) = %{tl_version}

%description -n texlive-boxhandler
The package allows the user to optimise presentation of LaTeX
tables and figures. Boxhandler will lay out table and figure
captions with a variety of stylistic apperances, and will also
allow figures and tables to be "wrapped" in a manner consistent
with many business and government documents. For a document
that might appear in different venues with different
formatting, boxhandler permits the creation of a LaTeX source
document that can, with a single-line change in the source
code, produce an output that has very different layout from the
baseline configuration, not only in terms of caption style, but
more importantly in terms of the locations where figures,
tables and lists appear (or not) in the document. Deferral
routines also allow one to keep all figure and table data in a
separate source file, while nonetheless producing a document
with figures and tables appearing in the desired location.

%package -n texlive-boxhandler-doc
Summary:        Documentation for boxhandler
Version:        svn28031.1.30

Provides:       tex-boxhandler-doc
AutoReqProv:    No

%description -n texlive-boxhandler-doc
Documentation for boxhandler

%package -n texlive-bpchem
Provides:       tex-bpchem = %{tl_version}
License:        LPPL
Summary:        Typeset chemical names, formulae, etc
Version:        svn45120
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xspace.sty), tex(lgrenc.def)
Provides:       tex(bpchem.sty) = %{tl_version}

%description -n texlive-bpchem
The package provides support for typesetting simple chemical
formulae, those long IUPAC compound names, and some chemical
idioms. It also supports the labelling of compounds and
reference to labelled compounds.

%package -n texlive-bpchem-doc
Summary:        Documentation for bpchem
Version:        svn45120
Provides:       tex-bpchem-doc
AutoReqProv:    No

%description -n texlive-bpchem-doc
Documentation for bpchem

%package -n texlive-bpolynomial
Provides:       tex-bpolynomial = %{tl_version}
License:        LPPL
Summary:        Drawing polynomial functions of up to order 3
Version:        svn15878.0.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-bpolynomial
This MetaPost package helps plotting polynomial and root
functions up to order three. The package provides macros to
calculate Bezier curves exactly matching a given constant,
linear, quadratic or cubic polynomial, or square or cubic root
function. In addition, tangents on all functions and
derivatives of polynomials can be calculated.

%package -n texlive-bpolynomial-doc
Summary:        Documentation for bpolynomial
Version:        svn15878.0.5

Provides:       tex-bpolynomial-doc
AutoReqProv:    No

%description -n texlive-bpolynomial-doc
Documentation for bpolynomial

%package -n texlive-bracketkey
Provides:       tex-bracketkey = %{tl_version}
License:        LPPL 1.3
Summary:        Produce bracketed identification keys
Version:        svn17129.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bracketkey.sty) = %{tl_version}

%description -n texlive-bracketkey
The package provides an environment bracketkey for use when
producing lists of species.

%package -n texlive-bracketkey-doc
Summary:        Documentation for bracketkey
Version:        svn17129.1.0

Provides:       tex-bracketkey-doc
AutoReqProv:    No

%description -n texlive-bracketkey-doc
Documentation for bracketkey

%package -n texlive-braids
Provides:       tex-braids = %{tl_version}
License:        LPPL 1.3
Summary:        Draw braid diagrams with PGF/TikZ
Version:        svn23790.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(braids.sty) = %{tl_version}

%description -n texlive-braids
The package enables drawing of braid diagrams with PGF/TikZ
using a simple syntax. The braid itself is specified by giving
a word in the braid group, and there are many options for
styling the strands and for drawing "floors".

%package -n texlive-braids-doc
Summary:        Documentation for braids
Version:        svn23790.1.0

Provides:       tex-braids-doc
AutoReqProv:    No

%description -n texlive-braids-doc
Documentation for braids

%package -n texlive-braille
Provides:       tex-braille = %{tl_version}
License:        LPPL
Summary:        Support for braille
Version:        svn20655.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(braille.sty) = %{tl_version}

%description -n texlive-braille
This package allows the user to produce Braille documents on
paper for the blind without knowing Braille (which can take
years to learn). Python scripts grade1.py and grade2.py convert
ordinary text to grade 1 and 2 Braille tags; then, the LaTeX
package takes the tags and prints out corresponding Braille
symbols.

%package -n texlive-braille-doc
Summary:        Documentation for braille
Version:        svn20655.0

Provides:       tex-braille-doc
AutoReqProv:    No

%description -n texlive-braille-doc
Documentation for braille

%package -n texlive-braket
Provides:       tex-braket = %{tl_version}
License:        Public Domain
Summary:        Dirac bra-ket and set notations
Version:        svn17127.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(braket.sty) = %{tl_version}

%description -n texlive-braket
Provides macros to typeset bra-ket notation, as well as set
specifiers, with a single ("|") or a double ("||" or ("\|")
vertical bar specifier in between two bracketed parts. Each
macro comes in a fixed-size version and an expanding version.
If the package finds itself operating under e-tex, it uses the
extended primitive \middle for more reliable results

%package -n texlive-braket-doc
Summary:        Documentation for braket
Version:        svn17127.0

Provides:       tex-braket-doc
AutoReqProv:    No

%description -n texlive-braket-doc
Documentation for braket

%package -n texlive-brandeis-dissertation
Provides:       tex-brandeis-dissertation = %{tl_version}
License:        LPPL 1.2
Summary:        Class for Brandeis University dissertations
Version:        svn32047.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(setspace.sty), tex(geometry.sty)
Provides:       tex(brandeis-dissertation.cls) = %{tl_version}

%description -n texlive-brandeis-dissertation
The class will enable the user to typeset a dissertation which
adheres to the formatting guidelines of Brandeis University
Graduate School of Arts and Sciences (GSAS).

%package -n texlive-brandeis-dissertation-doc
Summary:        Documentation for brandeis-dissertation
Version:        svn32047.2.0

Provides:       tex-brandeis-dissertation-doc
AutoReqProv:    No

%description -n texlive-brandeis-dissertation-doc
Documentation for brandeis-dissertation

%package -n texlive-breakurl
Provides:       tex-breakurl = %{tl_version}
License:        LPPL
Summary:        Line-breakable \url-like links in hyperref when compiling via dvips/ps2pdf
Version:        svn29901.1.40

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(xkeyval.sty), tex(ifpdf.sty)
Provides:       tex(breakurl.sty) = %{tl_version}

%description -n texlive-breakurl
This package provides a command much like hyperref's \url that
typesets a URL using a typewriter-like font. However, if the
dvips driver is being used, the original \url doesn't allow
line breaks in the middle of the created link: the link comes
in one atomic piece. This package allows such line breaks in
the generated links.

%package -n texlive-breakurl-doc
Summary:        Documentation for breakurl
Version:        svn29901.1.40

Provides:       tex-breakurl-doc
AutoReqProv:    No

%description -n texlive-breakurl-doc
Documentation for breakurl

%package -n texlive-breqn
Provides:       tex-breqn = %{tl_version}
License:        LPPL 1.3
Summary:        Automatic line breaking of displayed equations
Version:        svn43071
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(keyval.sty), tex(calc.sty)
Provides:       tex(breqn.sty) = %{tl_version}, tex(flexisym.sty) = %{tl_version}
Provides:       tex(mathstyle.sty) = %{tl_version}

%description -n texlive-breqn
The package provides solutions to a number of common
difficulties in writing displayed equations and getting high-
quality output. For example, it is a well-known inconvenience
that if an equation must be broken into more than one line,
'left...right' constructs cannot span lines. The breqn package
makes them work as one would expect whether or not there is an
intervening line break. The single most ambitious goal of the
package, however, is to support automatic linebreaking of
displayed equations. Such linebreaking cannot be done without
substantial changes under the hood in the way formulae are
processed; the code must be watched carefully, keeping an eye
on possible glitches. The bundle also contains the flexisym and
mathstyle packages, which are both designated as support for
breqn.

%package -n texlive-breqn-doc
Summary:        Documentation for breqn
Version:        svn43071
Provides:       tex-breqn-doc
AutoReqProv:    No

%description -n texlive-breqn-doc
Documentation for breqn

%package -n texlive-br-lex
Provides:       tex-br-lex = %{tl_version}
License:        LPPL 1.3
Summary:        A Class for Typesetting Brazilian legal texts
Version:        svn44939
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(enumitem.sty), tex(indentfirst.sty), tex(easylist.sty), tex(ulem.sty)
Requires:       tex(nowidow.sty), tex(ifxetex.sty), tex(fontspec.sty), tex(polyglossia.sty)
Requires:       tex(inputenc.sty), tex(babel.sty), tex(titlesec.sty), tex(etoolbox.sty)
Provides:       tex(br-lex.cls) = %{tl_version}

%description -n texlive-br-lex
This class implements rules to typeset Brazilian legal texts.
Its purpose is to be an easy-to-use implementation for the end-
user.

%package -n texlive-br-lex-doc
Summary:        Documentation for br-lex
Version:        svn44939
Provides:       tex-br-lex-doc
AutoReqProv:    No

%description -n texlive-br-lex-doc
Documentation for br-lex

%package -n texlive-bropd
Provides:       tex-bropd = %{tl_version}
License:        LPPL 1.3
Summary:        Simplified brackets and differentials in LaTeX
Version:        svn35383.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bropd.sty) = %{tl_version}

%description -n texlive-bropd
The package simplifies the process of writing differential
operators and brackets in LaTeX. The commands facilitate the
easy manipulation of equations involving brackets and allow
partial differentials to be expressed in an alternate form.

%package -n texlive-bropd-doc
Summary:        Documentation for bropd
Version:        svn35383.1.2

Provides:       tex-bropd-doc
AutoReqProv:    No

%description -n texlive-bropd-doc
Documentation for bropd

%package -n texlive-brushscr
Provides:       tex-brushscr = %{tl_version}
License:        Public Domain
Summary:        A handwriting script font
Version:        svn28363.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(pbsi.map) = %{tl_version}, tex(pbsi.tfm) = %{tl_version}
Provides:       tex(pbsi8r.tfm) = %{tl_version}, tex(pbsi8t.tfm) = %{tl_version}
Provides:       tex(BrushScriptX-Italic.pfa) = %{tl_version}
Provides:       tex(pbsi8t.vf) = %{tl_version}, tex(pbsi.sty) = %{tl_version}
Provides:       tex(t1pbsi.fd) = %{tl_version}

%description -n texlive-brushscr
The BrushScript font simulates hand-written characters; it is
distributed in Adobe Type 1 format (but is available in italic
shape only). The package includes the files needed by LaTeX in
order to use that font. The file AAA_readme.tex fully describes
the package and sample.tex illustrates its use.

%package -n texlive-brushscr-doc
Summary:        Documentation for brushscr
Version:        svn28363.0

Provides:       tex-brushscr-doc
AutoReqProv:    No

%description -n texlive-brushscr-doc
Documentation for brushscr

%package -n texlive-bullcntr
Provides:       tex-bullcntr = %{tl_version}
License:        LPPL 1.3
Summary:        Display list item counter as regular pattern of bullets
Version:        svn15878.0.04

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bullcntr.sty) = %{tl_version}, tex(bullenum.sty) = %{tl_version}

%description -n texlive-bullcntr
The bullcntr package defines the command bullcntr, which may be
thought of as an analogue of the \fnsymbol command: like the
latter, it displays the value of a counter lying between 1 and
9, but uses, for the purpose, a regular pattern of bullets.

%package -n texlive-bullcntr-doc
Summary:        Documentation for bullcntr
Version:        svn15878.0.04

Provides:       tex-bullcntr-doc
AutoReqProv:    No

%description -n texlive-bullcntr-doc
Documentation for bullcntr

%package -n texlive-burmese
Provides:       tex-burmese = %{tl_version}
License:        LPPL
Summary:        Basic Support for Writing Burmese
Version:        svn25185.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(relsize.sty)
Provides:       tex(burmese.map) = %{tl_version}, tex(burm.tfm) = %{tl_version}
Provides:       tex(burm.pfb) = %{tl_version}, tex(birm.sty) = %{tl_version}
Provides:       tex(ubirm.fd) = %{tl_version}

%description -n texlive-burmese
This package provides basic support for writing Burmese. The
package provides a preprocessor (written in Perl), an Adobe
Type 1 font, and LaTeX macros.

%package -n texlive-burmese-doc
Summary:        Documentation for burmese
Version:        svn25185.0

Provides:       tex-burmese-doc
AutoReqProv:    No

%description -n texlive-burmese-doc
Documentation for burmese

%package -n texlive-bussproofs
Provides:       tex-bussproofs = %{tl_version}
License:        LPPL 1.3
Summary:        Proof trees in the style of the sequent calculus
Version:        svn27488.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bussproofs.sty) = %{tl_version}

%description -n texlive-bussproofs
The package allows the construction of proof trees in the style
of the sequent calculus and many other proof systems. One novel
feature of the macros is they support the horizontal alignment
according to some centre point specified with the command
\fCenter. This is the style often used in sequent calculus
proofs. The package works in a Plain TeX document, as well as
in LaTeX; an exposition of the commands available is given in
the package file itself.

%package -n texlive-bussproofs-doc
Summary:        Documentation for bussproofs
Version:        svn27488.1.1

Provides:       tex-bussproofs-doc
AutoReqProv:    No

%description -n texlive-bussproofs-doc
Documentation for bussproofs

%package -n texlive-bxbase
Provides:       tex-bxbase = %{tl_version}
License:        MIT
Summary:        BX bundle base components
Version:        svn44481
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifxetex.sty)
Provides:       tex(bxbase.def) = %{tl_version}, tex(bxbase.sty) = %{tl_version}
Provides:       tex(bxucs.sty) = %{tl_version}, tex(bxutf8.def) = %{tl_version}
Provides:       tex(bxutf8x.def) = %{tl_version}, tex(zxbase.sty) = %{tl_version}

%description -n texlive-bxbase
The main purpose of this bundle is to serve as an underlying
library for other packages created by the same author (their
names start with "BX" or "PX"). However bxbase package contains
a few user-level commands and is of some use by itself.

%package -n texlive-bxbase-doc
Summary:        Documentation for bxbase
Version:        svn44481
Provides:       tex-bxbase-doc
AutoReqProv:    No

%description -n texlive-bxbase-doc
Documentation for bxbase

%package -n texlive-bxcjkjatype
Provides:       tex-bxcjkjatype = %{tl_version}
License:        MIT
Summary:        Typeset Japanese with pdfLaTeX and CJK
Version:        svn42292
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(keyval.sty), tex(CJK.sty), tex(CJKutf8.sty), tex(CJKspace.sty)
Requires:       tex(CJKpunct.sty), tex(etoolbox.sty), tex(atbegshi.sty)
Provides:       tex(bxcjkjatype.sty) = %{tl_version}

%description -n texlive-bxcjkjatype
The package provides a working configuration of the CJK
package, suitable for Japanese typesetting of moderate quality.
Moreover, it facilitates use of the CJK package for pLaTeX
users, by providing commands that are similar to those used by
the pLaTeX kernel and some other packages used with it.

%package -n texlive-bxcjkjatype-doc
Summary:        Documentation for bxcjkjatype
Version:        svn42292
Provides:       tex-bxcjkjatype-doc
AutoReqProv:    No

%description -n texlive-bxcjkjatype-doc
Documentation for bxcjkjatype

%package -n texlive-bxdpx-beamer
Provides:       tex-bxdpx-beamer = %{tl_version}
License:        MIT
Summary:        Dvipdfmx extras for use with beamer
Version:        svn41813
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bxdpx-beamer.sty) = %{tl_version}

%description -n texlive-bxdpx-beamer
The package is a driver to support beamer Navigation symbols
and \framezoomed regions when using dvipdfmx as PDF generator
(e.g., as part of e-pTeX). The package does not define any
'user' commands.

%package -n texlive-bxdpx-beamer-doc
Summary:        Documentation for bxdpx-beamer
Version:        svn41813
Provides:       tex-bxdpx-beamer-doc
AutoReqProv:    No

%description -n texlive-bxdpx-beamer-doc
Documentation for bxdpx-beamer

%package -n texlive-bxeepic
Provides:       tex-bxeepic = %{tl_version}
License:        MIT
Summary:        Eepic facilities using pict2e
Version:        svn30559.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pict2e.sty)
Provides:       tex(bxdpxp2e.def) = %{tl_version}, tex(bxeepic.sty) = %{tl_version}

%description -n texlive-bxeepic
The package provides an eepic driver to use pict2e facilities.

%package -n texlive-bxeepic-doc
Summary:        Documentation for bxeepic
Version:        svn30559.0.2

Provides:       tex-bxeepic-doc
AutoReqProv:    No

%description -n texlive-bxeepic-doc
Documentation for bxeepic

%package -n texlive-bxjscls
Provides:       tex-bxjscls = %{tl_version}
License:        BSD
Summary:        Japanese document class collection for all major engines
Version:        svn48235
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(calc.sty), tex(keyval.sty), tex(type1cm.sty), tex(geometry.sty)
Provides:       tex(bxjsarticle.cls) = %{tl_version}, tex(bxjsbook.cls) = %{tl_version}
Provides:       tex(bxjsja-minimal.def) = %{tl_version}, tex(bxjsja-standard.def) = %{tl_version}
Provides:       tex(bxjsreport.cls) = %{tl_version}, tex(bxjsslide.cls) = %{tl_version}

%description -n texlive-bxjscls
This package provides an extended version of the Japanese
document class collection provided by jsclasses. While the
original version supports only pLaTeX and upLaTeX, the extended
version also supports pdfLaTeX, XeLaTeX and LuaLaTeX, with the
aid of suitable packages that provide capability of Japanese
typesetting.

%package -n texlive-bxjscls-doc
Summary:        Documentation for bxjscls
Version:        svn48235
Provides:       tex-bxjscls-doc
AutoReqProv:    No

%description -n texlive-bxjscls-doc
Documentation for bxjscls

%package -n texlive-bxpdfver
Provides:       tex-bxpdfver = %{tl_version}
License:        MIT
Summary:        Specify version and compression level of output PDF files
Version:        svn43201
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(atbegshi.sty)
Provides:       tex(bxpdfver.sty) = %{tl_version}

%description -n texlive-bxpdfver
This package enables users to specify in their sources the
following settings on the PDF document to output: PDF version
(1.4, 1.5 etc.); whether or not to compress streams; whether or
not to use object streams. This package supports all major PDF-
output engines and dvipdfmx.

%package -n texlive-bxpdfver-doc
Summary:        Documentation for bxpdfver
Version:        svn43201
Provides:       tex-bxpdfver-doc
AutoReqProv:    No

%description -n texlive-bxpdfver-doc
Documentation for bxpdfver

%package -n texlive-bytefield
Provides:       tex-bytefield = %{tl_version}
License:        LPPL
Summary:        Create illustrations for network protocol specifications
Version:        svn45339
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(calc.sty), tex(keyval.sty)
Provides:       tex(bytefield.sty) = %{tl_version}, tetex-bytefield = %{tl_version}
Obsoletes:      tetex-bytefield < %{tl_version}

%description -n texlive-bytefield
The bytefield package helps the user create illustrations for
network protocol specifications and anything else that utilizes
fields of data. These illustrations show how the bits and bytes
are laid out in a packet or in memory. Users should note that
the present version 2.0 offers a different (and incompatible)
user interface from earlier versions.

%package -n texlive-bytefield-doc
Summary:        Documentation for bytefield
Version:        svn45339
Provides:       tex-bytefield-doc
AutoReqProv:    No

%description -n texlive-bytefield-doc
Documentation for bytefield

%package -n texlive-c90
Provides:       tex-c90 = %{tl_version}
License:        LPPL
Summary:        c90 package
Version:        svn45666
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(c90.enc) = %{tl_version}

%description -n texlive-c90
c90 package

%package -n texlive-c90-doc
Summary:        Documentation for c90
Version:        svn45666
Provides:       tex-c90-doc
AutoReqProv:    No

%description -n texlive-c90-doc
Documentation for c90

%package -n texlive-cabin
Provides:       tex-cabin = %{tl_version}
License:        OFL
Summary:        A humanist Sans Serif font, with LaTeX support
Version:        svn47770
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(ifxetex.sty)
Requires:       tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty), tex(fontspec.sty)
Requires:       tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(cbn_6vzwvh.enc) = %{tl_version}, tex(cbn_7kg2sc.enc) = %{tl_version}
Provides:       tex(cbn_aojlca.enc) = %{tl_version}, tex(cbn_cgvdav.enc) = %{tl_version}
Provides:       tex(cbn_dh6h6g.enc) = %{tl_version}, tex(cbn_eeshah.enc) = %{tl_version}
Provides:       tex(cbn_gi6ftn.enc) = %{tl_version}, tex(cbn_gipwm5.enc) = %{tl_version}
Provides:       tex(cbn_hvmmj2.enc) = %{tl_version}, tex(cbn_j5omty.enc) = %{tl_version}
Provides:       tex(cbn_jxvnp4.enc) = %{tl_version}, tex(cbn_mzrldx.enc) = %{tl_version}
Provides:       tex(cbn_x3x2zv.enc) = %{tl_version}, tex(cbn_xtln4x.enc) = %{tl_version}
Provides:       tex(cbn_xvjm53.enc) = %{tl_version}, tex(cbn_zljgjy.enc) = %{tl_version}
Provides:       tex(cabin.map) = %{tl_version}, tex(Cabin-Bold.otf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic.otf) = %{tl_version}
Provides:       tex(Cabin-Medium.otf) = %{tl_version}, tex(Cabin-MediumItalic.otf) = %{tl_version}
Provides:       tex(Cabin-Regular.otf) = %{tl_version}, tex(Cabin-RegularItalic.otf) = %{tl_version}
Provides:       tex(Cabin-SemiBold.otf) = %{tl_version}, tex(Cabin-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold.otf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic.otf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium.otf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic.otf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular.otf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic.otf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold.otf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic.otf) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-ly1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-ly1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-ot1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-ot1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Cabin-Bold.pfb) = %{tl_version}, tex(Cabin-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Cabin-Italic.pfb) = %{tl_version}, tex(Cabin-Medium.pfb) = %{tl_version}
Provides:       tex(Cabin-MediumItalic.pfb) = %{tl_version}
Provides:       tex(Cabin-Regular.pfb) = %{tl_version}, tex(Cabin-SemiBold.pfb) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-Bold.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-Medium.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-Regular.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold.pfb) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic.pfb) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Cabin-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Medium-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-MediumItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-RegularItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-ly1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-ot1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-sc-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(CabinCondensed-SemiBoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Cabin-TLF.fd) = %{tl_version}, tex(LY1CabinCondensed-TLF.fd) = %{tl_version}
Provides:       tex(OT1Cabin-TLF.fd) = %{tl_version}, tex(OT1CabinCondensed-TLF.fd) = %{tl_version}
Provides:       tex(T1Cabin-TLF.fd) = %{tl_version}, tex(T1CabinCondensed-TLF.fd) = %{tl_version}
Provides:       tex(TS1Cabin-TLF.fd) = %{tl_version}, tex(TS1CabinCondensed-TLF.fd) = %{tl_version}
Provides:       tex(cabin.sty) = %{tl_version}

%description -n texlive-cabin
Cabin is a humanist sans with four weights and true italics and
small capitals. According to the designer, Pablo Impallari,
Cabin was inspired by Edward Johnston's and Eric Gill's
typefaces, with a touch of modernism. Cabin incorporates modern
proportions, optical adjustments, and some elements of the
geometric sans. cabin.sty supports use of the font under LaTeX,
pdfLaTeX, xeLaTeX and luaLaTeX; it uses the mweights, to manage
the user's view of all those font weights. An sfdefault option
is provided to enable Cabin as the default text font. The
fontaxes package is required for use with [pdf]LaTeX.

%package -n texlive-cabin-doc
Summary:        Documentation for cabin
Version:        svn47770
Provides:       tex-cabin-doc
AutoReqProv:    No

%description -n texlive-cabin-doc
Documentation for cabin

%package -n texlive-caladea
Provides:       tex-caladea = %{tl_version}
License:        ASL 2.0
Summary:        Support for the Caladea family of fonts
Version:        svn34991.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty)
Provides:       tex(cld_cb3g7n.enc) = %{tl_version}, tex(cld_fjy5hl.enc) = %{tl_version}
Provides:       tex(cld_prieif.enc) = %{tl_version}, tex(cld_w45fff.enc) = %{tl_version}
Provides:       tex(caladea.map) = %{tl_version}, tex(Caladea-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Caladea-Bold.ttf) = %{tl_version}, tex(Caladea-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Caladea-Italic.ttf) = %{tl_version}, tex(Caladea-Regular.ttf) = %{tl_version}
Provides:       tex(Caladea-Bold.pfb) = %{tl_version}, tex(Caladea-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Caladea-Italic.pfb) = %{tl_version}, tex(Caladea-Regular.pfb) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Caladea-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Caladea-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Caladea-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Caladea-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Caladea-TLF.fd) = %{tl_version}, tex(OT1Caladea-TLF.fd) = %{tl_version}
Provides:       tex(T1Caladea-TLF.fd) = %{tl_version}, tex(TS1Caladea-TLF.fd) = %{tl_version}
Provides:       tex(caladea.sty) = %{tl_version}

%description -n texlive-caladea
This package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Caladea family of fonts, designed by Carolina
Giovagnoli and Andres Torresi of the Huerta Tipografica foundry
and adopted by Google for ChromeOS as a font-metric compatible
replacement for Cambria.

%package -n texlive-caladea-doc
Summary:        Documentation for caladea
Version:        svn34991.0

Provides:       tex-caladea-doc
AutoReqProv:    No

%description -n texlive-caladea-doc
Documentation for caladea

%package -n texlive-calcage
Provides:       tex-calcage = %{tl_version}
License:        LPPL 1.3
Summary:        Calculate the age of something, in years
Version:        svn27725.0.90

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(fnumprint.sty), tex(datenumber.sty), tex(fp.sty), tex(calc.sty)
Requires:       tex(xkeyval.sty), tex(kvoptions.sty), tex(xifthen.sty)
Provides:       tex(calcage.sty) = %{tl_version}

%description -n texlive-calcage
The package calculates the age of someone or something in
years. Internally it uses the datenumber package to calculate
the age in days; conversion from days to years is then
performed, taking care of leap years and such odd things.

%package -n texlive-calcage-doc
Summary:        Documentation for calcage
Version:        svn27725.0.90

Provides:       tex-calcage-doc
AutoReqProv:    No

%description -n texlive-calcage-doc
Documentation for calcage

%package -n texlive-calctab
Provides:       tex-calctab = %{tl_version}
License:        LPPL
Summary:        Language for numeric tables
Version:        svn15878.v0.6.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(alphalph.sty), tex(booktabs.sty), tex(eurosym.sty), tex(xcolor.sty)
Requires:       tex(numprint.sty), tex(xkeyval.sty), tex(ifthen.sty), tex(fltpoint.sty)
Requires:       tex(xstring.sty)
Provides:       tex(calctab.sty) = %{tl_version}

%description -n texlive-calctab
The calctab package helps the user to typeset a kind of
economic table such as invoices, expense notes and liquidation,
or other tabular material with a values column. The code
computes sum and percentage with floating point numeric methods
(using the fltpoint package) and builds the render table task.

%package -n texlive-calctab-doc
Summary:        Documentation for calctab
Version:        svn15878.v0.6.1

Provides:       tex-calctab-doc
AutoReqProv:    No

%description -n texlive-calctab-doc
Documentation for calctab

%package -n texlive-calculation
Provides:       tex-calculation = %{tl_version}
License:        LPPL 1.3
Summary:        Typesetting reasoned calculations, also called calculational proofs
Version:        svn35973.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(delarray.sty)
Provides:       tex(calculation.sty) = %{tl_version}

%description -n texlive-calculation
The calculation environment formats reasoned calculations, also
called calculational proofs. The notion of reasoned
calculations or calculational proofs was originally advocated
by Wim Feijen and Edsger Dijkstra. The package accepts options
fleqn and leqno (with the same effect as the LaTeX options
fleqn and leqno, or may inherit the options from the document
class). It allows steps and expressions to be numbered (by
LaTeX equation numbers, obeying the LaTeX \label command to
refer to these numbers), and a step doesn't take vertical space
if its hint is empty. An expression in a calculation can be
given a comment; it is placed at the side opposite to the
equation numbers. Calculations are allowed inside hints
although numbering and commenting is then disabled.

%package -n texlive-calculation-doc
Summary:        Documentation for calculation
Version:        svn35973.1.0

Provides:       tex-calculation-doc
AutoReqProv:    No

%description -n texlive-calculation-doc
Documentation for calculation

%package -n texlive-calculator
Provides:       tex-calculator = %{tl_version}
License:        LPPL 1.2
Summary:        Use LaTeX as a scientific calculator
Version:        svn33041.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(calculator.sty) = %{tl_version}, tex(calculus.sty) = %{tl_version}

%description -n texlive-calculator
The calculator and calculus packages define several
instructions which allow us to realise algebraic operations and
to evaluate elementary functions and derivatives in our
documents. The package's main goal is to define the arithmetic
and functional calculations need in the author's package
xpicture, but the numeric abilities of "calculator" and
"calculus" may be useful in other contexts.

%package -n texlive-calculator-doc
Summary:        Documentation for calculator
Version:        svn33041.2.0

Provides:       tex-calculator-doc
AutoReqProv:    No

%description -n texlive-calculator-doc
Documentation for calculator

%package -n texlive-calligra
Provides:       tex-calligra = %{tl_version}
License:        Copyright only
Summary:        Calligraphic font
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(callig15.tfm) = %{tl_version}

%description -n texlive-calligra
A calligraphic font in the handwriting style of the author,
Peter Vanroose. The font is supplied as Metafont source. LaTeX
support of the font is provided in the calligra package in the
fundus bundle.

%package -n texlive-calligra-doc
Summary:        Documentation for calligra
Version:        svn15878.0

Provides:       tex-calligra-doc
AutoReqProv:    No

%description -n texlive-calligra-doc
Documentation for calligra

%package -n texlive-calligra-type1
Provides:       tex-calligra-type1 = %{tl_version}
License:        Copyright only
Summary:        Type 1 version of Calligra
Version:        svn24302.001.000

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(calligra.map) = %{tl_version}, tex(callig15.pfb) = %{tl_version}

%description -n texlive-calligra-type1
This is a conversion (using mf2pt1) of Peter Vanroose's
handwriting font.

%package -n texlive-calligra-type1-doc
Summary:        Documentation for calligra-type1
Version:        svn24302.001.000

Provides:       tex-calligra-type1-doc
AutoReqProv:    No

%description -n texlive-calligra-type1-doc
Documentation for calligra-type1

%package -n texlive-calrsfs
Provides:       tex-calrsfs = %{tl_version}
License:        Public Domain
Summary:        Copperplate calligraphic letters in LaTeX
Version:        svn17125.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(OMSrsfs.fd) = %{tl_version}, tex(calrsfs.sty) = %{tl_version}

%description -n texlive-calrsfs
Provides a maths interface to the rsfs fonts.

%package -n texlive-calrsfs-doc
Summary:        Documentation for calrsfs
Version:        svn17125.0

Provides:       tex-calrsfs-doc
AutoReqProv:    No

%description -n texlive-calrsfs-doc
Documentation for calrsfs

%package -n texlive-cals
Provides:       tex-cals = %{tl_version}
License:        LPPL 1.3
Summary:        Multipage tables with wide range of features
Version:        svn43003
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cals.sty) = %{tl_version}

%description -n texlive-cals
The package allows the user to typeset multipage tables with
repeatable headers and footers, and with cells spanned over
rows and columns. Decorations are supported: padding,
background color, width of separation rules. The package is
compatible with multicol and pdfsync.

%package -n texlive-cals-doc
Summary:        Documentation for cals
Version:        svn43003
Provides:       tex-cals-doc
AutoReqProv:    No

%description -n texlive-cals-doc
Documentation for cals

%package -n texlive-calxxxx-yyyy
Provides:       tex-calxxxx-yyyy = %{tl_version}
License:        LPPL 1.3
Summary:        Print a calendar for a group of years
Version:        svn46198
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(calxxxx-yyyy.tex) = %{tl_version}

%description -n texlive-calxxxx-yyyy
The package prints a calendar for 2 or more years, according to
a language selection. The package is also "culture dependent",
in the sense that it will start weeks according to local rules:
e.g., weeks conventionally start on Monday in the English-
speaking world.

%package -n texlive-calxxxx-yyyy-doc
Summary:        Documentation for calxxxx-yyyy
Version:        svn46198
Provides:       tex-calxxxx-yyyy-doc
AutoReqProv:    No

%description -n texlive-calxxxx-yyyy-doc
Documentation for calxxxx-yyyy

%package -n texlive-cancel
Provides:       tex-cancel = %{tl_version}
License:        Public Domain
Summary:        Place lines through maths formulae
Version:        svn32508.2.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cancel.sty) = %{tl_version}

%description -n texlive-cancel
A package to draw diagonal lines ("cancelling" a term) and
arrows with limits (cancelling a term "to a value") through
parts of maths formulae.

%package -n texlive-cancel-doc
Summary:        Documentation for cancel
Version:        svn32508.2.2

Provides:       tex-cancel-doc
AutoReqProv:    No

%description -n texlive-cancel-doc
Documentation for cancel

%package -n texlive-canoniclayout
Provides:       tex-canoniclayout = %{tl_version}
License:        LPPL 1.3
Summary:        Create canonical page layouts with memoir
Version:        svn24523.0.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(canoniclayout.sty) = %{tl_version}

%description -n texlive-canoniclayout
A canonic text layout has specified relations to a circle
inscribed within the enclosing page. The package allows the
user to use a canonic layout with the memoir class.

%package -n texlive-canoniclayout-doc
Summary:        Documentation for canoniclayout
Version:        svn24523.0.4

Provides:       tex-canoniclayout-doc
AutoReqProv:    No

%description -n texlive-canoniclayout-doc
Documentation for canoniclayout

%package -n texlive-cantarell
Provides:       tex-cantarell = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX support for the Cantarell font family
Version:        svn27066.2.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(keyval.sty), tex(slantsc.sty)
Provides:       tex(cantarell-01.enc) = %{tl_version}, tex(cantarell-02.enc) = %{tl_version}
Provides:       tex(cantarell-03.enc) = %{tl_version}, tex(cantarell.map) = %{tl_version}
Provides:       tex(Cantarell-Bold-01.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-02.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-03.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-01.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-02.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-03.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-ts1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-01.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-02.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-03.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-01.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-02.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-03.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-ts1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-ot1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-t1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-t2a.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-t2b.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-t2c.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-ts1.tfm) = %{tl_version}
Provides:       tex(Cantarell-Regular-x2.tfm) = %{tl_version}
Provides:       tex(Cantarell-Bold.pfb) = %{tl_version}, tex(Cantarell-Regular.pfb) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-Slanted-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-ts1.vf) = %{tl_version}
Provides:       tex(Cantarell-Bold-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-ts1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-Slanted-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-SmallCaps-x2.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-ot1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-t1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-t2a.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-t2b.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-t2c.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-ts1.vf) = %{tl_version}
Provides:       tex(Cantarell-Regular-x2.vf) = %{tl_version}
Provides:       tex(cantarell.sty) = %{tl_version}, tex(ot1fca.fd) = %{tl_version}
Provides:       tex(t1fca.fd) = %{tl_version}, tex(t2afca.fd) = %{tl_version}
Provides:       tex(t2bfca.fd) = %{tl_version}, tex(t2cfca.fd) = %{tl_version}
Provides:       tex(ts1fca.fd) = %{tl_version}, tex(x2fca.fd) = %{tl_version}

%description -n texlive-cantarell
Cantarell is a contemporary Humanist sans serif designed by
Dave Crossland and Jakub Steiner. This font, delivered under
the OFL version 1.1, is available on the GNOME download server.
The present package provides support for this font in LaTeX. It
includes Type 1 versions of the fonts, converted for this
package using FontForge from its sources, for full support with
Dvips.

%package -n texlive-cantarell-doc
Summary:        Documentation for cantarell
Version:        svn27066.2.4

Provides:       tex-cantarell-doc
AutoReqProv:    No

%description -n texlive-cantarell-doc
Documentation for cantarell

%package -n texlive-captcont
Provides:       tex-captcont = %{tl_version}
License:        LPPL
Summary:        Retain float number across several floats
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(captcont.sty) = %{tl_version}

%description -n texlive-captcont
The captcont package provides the ability to continue the
numbering in your float environment (figure, table, etc.) with
minimal overhead. This package adds three commands: \caption*,
\captcont, and \captcont*. Along with the \caption command,
these give full control over the caption numbering, caption
text and the entries in the list-of pages. The \caption and
\captcont commands generate list-of page entries. The \caption
and \caption* commands increment the figure or table counter.
Captcont also fully supports the subfigure package.

%package -n texlive-captcont-doc
Summary:        Documentation for captcont
Version:        svn15878.2.0

Provides:       tex-captcont-doc
AutoReqProv:    No

%description -n texlive-captcont-doc
Documentation for captcont

%package -n texlive-captdef
Provides:       tex-captdef = %{tl_version}
License:        LPPL
Summary:        Declare free-standing \caption commands
Version:        svn17353.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(captdef.sty) = %{tl_version}

%description -n texlive-captdef
The \DeclareCaption command defines a class of caption command
associated with the counter specified to the command. These
commands are free-standing (i.e., don't need to be inside a
float environment). The package uses \DeclareCaption to define
\figcaption and \tabcaption, which can be used outside figure
or table environments.

%package -n texlive-captdef-doc
Summary:        Documentation for captdef
Version:        svn17353.0

Provides:       tex-captdef-doc
AutoReqProv:    No

%description -n texlive-captdef-doc
Documentation for captdef

%package -n texlive-caption
Provides:       tex-caption = %{tl_version}
License:        LPPL 1.3
Summary:        Customising captions in floating environments
Version:        svn47968
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(caption3.sty), tex(keyval.sty), tex(xspace.sty)
Provides:       tex(bicaption.sty) = %{tl_version}, tex(caption.sty) = %{tl_version}
Provides:       tex(caption2.sty) = %{tl_version}, tex(caption3.sty) = %{tl_version}
Provides:       tex(ltcaption.sty) = %{tl_version}, tex(newfloat.sty) = %{tl_version}
Provides:       tex(subcaption.sty) = %{tl_version}, tex(totalcount.sty) = %{tl_version}

%description -n texlive-caption
The caption package provides many ways to customise the
captions in floating environments like figure and table, and
cooperates with many other packages. Facilities include
rotating captions, sideways captions, continued captions (for
tables or figures that come in several parts). A list of
compatibility notes, for other packages, is provided in the
documentation. The package also provides the "caption outside
float" facility, in the same way that simpler packages like
capt-of do. The package supersedes caption2.

%package -n texlive-caption-doc
Summary:        Documentation for caption
Version:        svn47968
Provides:       tex-caption-doc
AutoReqProv:    No

%description -n texlive-caption-doc
Documentation for caption

%package -n texlive-capt-of
Provides:       tex-capt-of = %{tl_version}
License:        LPPL
Summary:        Captions on more than floats
Version:        svn29803.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(capt-of.sty) = %{tl_version}

%description -n texlive-capt-of
Defines a command \captionof for putting a caption to something
that's not a float. Note that the caption package includes a
\captionof command that is an extension of that provided by
this package.

%package -n texlive-capt-of-doc
Summary:        Documentation for capt-of
Version:        svn29803.0

Provides:       tex-capt-of-doc
AutoReqProv:    No

%description -n texlive-capt-of-doc
Documentation for capt-of

%package -n texlive-carlisle
Provides:       tex-carlisle = %{tl_version}
License:        LPPL
Summary:        David Carlisle's small packages
Version:        svn47876
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(color.sty), tex(tabularx.sty), tex(longtable.sty)
Provides:       tex(dotlessj.sty) = %{tl_version}, tex(ltxtable.sty) = %{tl_version}
Provides:       tex(plain.sty) = %{tl_version}, tex(remreset.sty) = %{tl_version}
Provides:       tex(scalefnt.sty) = %{tl_version}, tex(slashed.sty) = %{tl_version}

%description -n texlive-carlisle
Many of David Carlisle's more substantial packages stand on
their own, or as part of the LaTeX tools set; this set
contains: Making dotless 'j' characters for fonts that don't
have them; Fix marks in 2-column output; A method for combining
the capabilities of longtable and tabularx; A proforma for
building personalised LaTeX formats; A jiffy to suppress page
numbers; An environment for including Plain TeX in LaTeX
documents; A jiffy to remove counters from other counters'
reset lists; A package to rescale fonts to arbitrary sizes; A
jiffy to create 'slashed' characters for physicists; and An
environment for including HTML in LaTeX documents.

%package -n texlive-carlisle-doc
Summary:        Documentation for carlisle
Version:        svn47876
Provides:       tex-carlisle-doc
AutoReqProv:    No

%description -n texlive-carlisle-doc
Documentation for carlisle

%package -n texlive-carlito
Provides:       tex-carlito = %{tl_version}
License:        OFL
Summary:        Support for Carlito sans-serif fonts
Version:        svn35002.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty)
Provides:       tex(crlt_57h366.enc) = %{tl_version}, tex(crlt_bxv5ge.enc) = %{tl_version}
Provides:       tex(crlt_cegsyz.enc) = %{tl_version}, tex(crlt_csjzgd.enc) = %{tl_version}
Provides:       tex(crlt_eckivh.enc) = %{tl_version}, tex(crlt_houcxd.enc) = %{tl_version}
Provides:       tex(crlt_ibktmo.enc) = %{tl_version}, tex(crlt_lllwh4.enc) = %{tl_version}
Provides:       tex(crlt_llspvt.enc) = %{tl_version}, tex(crlt_n2dr37.enc) = %{tl_version}
Provides:       tex(crlt_n75whf.enc) = %{tl_version}, tex(crlt_ntvnfo.enc) = %{tl_version}
Provides:       tex(crlt_o4ofpw.enc) = %{tl_version}, tex(crlt_orgsld.enc) = %{tl_version}
Provides:       tex(crlt_rekp6x.enc) = %{tl_version}, tex(crlt_sghv4p.enc) = %{tl_version}
Provides:       tex(crlt_ssbojb.enc) = %{tl_version}, tex(crlt_uuhkl6.enc) = %{tl_version}
Provides:       tex(crlt_ynpzot.enc) = %{tl_version}, tex(crlt_z7vml3.enc) = %{tl_version}
Provides:       tex(carlito.map) = %{tl_version}, tex(Carlito-Bold-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-inf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-sup-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-inf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-sup-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-inf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-inf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-inf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-inf-t1.tfm) = %{tl_version}, tex(Carlito-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-lf-ot1.tfm) = %{tl_version}, tex(Carlito-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-lf-t1.tfm) = %{tl_version}, tex(Carlito-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-lf-ts1.tfm) = %{tl_version}, tex(Carlito-osf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-osf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-osf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-osf-t1.tfm) = %{tl_version}, tex(Carlito-osf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-osf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-sup-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-sup-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-sup-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-sup-t1.tfm) = %{tl_version}, tex(Carlito-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-tlf-t1.tfm) = %{tl_version}, tex(Carlito-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-tosf-ly1.tfm) = %{tl_version}
Provides:       tex(Carlito-tosf-ot1.tfm) = %{tl_version}
Provides:       tex(Carlito-tosf-t1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-tosf-t1.tfm) = %{tl_version}
Provides:       tex(Carlito-tosf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Carlito-tosf-ts1.tfm) = %{tl_version}
Provides:       tex(Carlito-Bold.ttf) = %{tl_version}, tex(Carlito-BoldItalic.ttf) = %{tl_version}
Provides:       tex(Carlito-Italic.ttf) = %{tl_version}, tex(Carlito-Regular.ttf) = %{tl_version}
Provides:       tex(Carlito-Bold.pfb) = %{tl_version}, tex(Carlito-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Carlito-Italic.pfb) = %{tl_version}, tex(Carlito.pfb) = %{tl_version}
Provides:       tex(Carlito-Bold-inf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-osf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-sup-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Bold-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-inf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-sup-t1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-BoldItalic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-inf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-lf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-osf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-sup-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-Italic-tosf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-inf-t1.vf) = %{tl_version}, tex(Carlito-lf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-lf-ts1.vf) = %{tl_version}, tex(Carlito-osf-t1.vf) = %{tl_version}
Provides:       tex(Carlito-osf-ts1.vf) = %{tl_version}, tex(Carlito-sup-t1.vf) = %{tl_version}
Provides:       tex(Carlito-tlf-t1.vf) = %{tl_version}, tex(Carlito-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Carlito-tosf-t1.vf) = %{tl_version}, tex(Carlito-tosf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Carlito-Inf.fd) = %{tl_version}, tex(LY1Carlito-LF.fd) = %{tl_version}
Provides:       tex(LY1Carlito-OsF.fd) = %{tl_version}, tex(LY1Carlito-Sup.fd) = %{tl_version}
Provides:       tex(LY1Carlito-TLF.fd) = %{tl_version}, tex(LY1Carlito-TOsF.fd) = %{tl_version}
Provides:       tex(OT1Carlito-Inf.fd) = %{tl_version}, tex(OT1Carlito-LF.fd) = %{tl_version}
Provides:       tex(OT1Carlito-OsF.fd) = %{tl_version}, tex(OT1Carlito-Sup.fd) = %{tl_version}
Provides:       tex(OT1Carlito-TLF.fd) = %{tl_version}, tex(OT1Carlito-TOsF.fd) = %{tl_version}
Provides:       tex(T1Carlito-Inf.fd) = %{tl_version}, tex(T1Carlito-LF.fd) = %{tl_version}
Provides:       tex(T1Carlito-OsF.fd) = %{tl_version}, tex(T1Carlito-Sup.fd) = %{tl_version}
Provides:       tex(T1Carlito-TLF.fd) = %{tl_version}, tex(T1Carlito-TOsF.fd) = %{tl_version}
Provides:       tex(TS1Carlito-LF.fd) = %{tl_version}, tex(TS1Carlito-OsF.fd) = %{tl_version}
Provides:       tex(TS1Carlito-TLF.fd) = %{tl_version}, tex(TS1Carlito-TOsF.fd) = %{tl_version}
Provides:       tex(carlito.sty) = %{tl_version}

%description -n texlive-carlito
The package provides LaTeX, pdfLaTeX, XeLaTeX and LuaLaTeX
support for the Carlito family of sans serif fonts, designed by
Lukasz Dziedzic of the tyPoland foundry and adopted by Google
for ChromeOS as a font-metric compatible replacement for
Calibri.

%package -n texlive-carlito-doc
Summary:        Documentation for carlito
Version:        svn35002.0

Provides:       tex-carlito-doc
AutoReqProv:    No

%description -n texlive-carlito-doc
Documentation for carlito

%package -n texlive-carolmin-ps
Provides:       tex-carolmin-ps = %{tl_version}
License:        LPPL
Summary:        Adobe Type 1 format of Carolingian Minuscule fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(cmin.map) = %{tl_version}, tex(cmin10.pfb) = %{tl_version}
Provides:       tex(cmin17.pfb) = %{tl_version}, tex(cmin7.pfb) = %{tl_version}
Provides:       tex(cminb10.pfb) = %{tl_version}, tex(cminb17.pfb) = %{tl_version}
Provides:       tex(cminb7.pfb) = %{tl_version}

%description -n texlive-carolmin-ps
The bundle offers Adobe Type 1 format versions of Peter
Wilson's Carolingian Minuscule font set (part of the bookhands
collection). The fonts in the bundle are ready-to-use
replacements for the Metafont originals.

%package -n texlive-carolmin-ps-doc
Summary:        Documentation for carolmin-ps
Version:        svn15878.0

Provides:       tex-carolmin-ps-doc
AutoReqProv:    No

%description -n texlive-carolmin-ps-doc
Documentation for carolmin-ps

%package -n texlive-cascadilla
Provides:       tex-cascadilla = %{tl_version}
License:        LPPL
Summary:        Typeset papers conforming to the stylesheet of the Cascadilla Proceedings Project
Version:        svn25144.1.8.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(geometry.sty), tex(times.sty), tex(indentfirst.sty)
Requires:       tex(fancyhdr.sty), tex(titlesec.sty), tex(natbib.sty), tex(caption.sty)
Provides:       tex(cascadilla.cls) = %{tl_version}

%description -n texlive-cascadilla
The class provides an extension of the standard LaTeX article
class that may be used to typeset papers conforming to the
stylesheet of the Cascadilla Proceedings Project, which is used
by a number of linguistics conference proceedings (e.g.,
WCCFL).

%package -n texlive-cascadilla-doc
Summary:        Documentation for cascadilla
Version:        svn25144.1.8.2

Provides:       tex-cascadilla-doc
AutoReqProv:    No

%description -n texlive-cascadilla-doc
Documentation for cascadilla

%package -n texlive-cases
Provides:       tex-cases = %{tl_version}
License:        Public Domain
Summary:        Numbered cases environment
Version:        svn17123.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cases.sty) = %{tl_version}

%description -n texlive-cases
Define the environment numcases: equations with several
alternative right-hand sides, with equation numbers for each
alternative. Also environment subnumcases, where each
alternative is a sub-number (e.g., 8a, 8b, ...) of the equation
set as a whole.

%package -n texlive-cases-doc
Summary:        Documentation for cases
Version:        svn17123.2.5

Provides:       tex-cases-doc
AutoReqProv:    No

%description -n texlive-cases-doc
Documentation for cases

%package -n texlive-casyl
Provides:       tex-casyl = %{tl_version}
License:        Public Domain
Summary:        Typeset Cree/Inuktitut in Canadian Aboriginal Syllabics
Version:        svn15878.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(casyll10.tfm) = %{tl_version}, tex(casyltex.sty) = %{tl_version}

%description -n texlive-casyl
The bundle constitutes a font (as Metafont source) and LaTeX
macros for its use within a document.

%package -n texlive-casyl-doc
Summary:        Documentation for casyl
Version:        svn15878.2.0

Provides:       tex-casyl-doc
AutoReqProv:    No

%description -n texlive-casyl-doc
Documentation for casyl

%package -n texlive-catchfilebetweentags
Provides:       tex-catchfilebetweentags = %{tl_version}
License:        LPPL 1.3
Summary:        Catch text delimited by docstrip tags
Version:        svn21476.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etex.sty), tex(etoolbox.sty), tex(ltxcmds.sty), tex(catchfile.sty)
Provides:       tex(catchfilebetweentags.sty) = %{tl_version}

%description -n texlive-catchfilebetweentags
This package (built using the facilities of catchfile) provides
a macro \catchfilebetweentags acts like the original \catchfile
but only extracts a portion of the file instead of the complete
file. The extracted portion can be delimited by strings or by
docstrip tags: %<*tag> .... %</tag> (comments in the caught
region may be included or dropped).

%package -n texlive-catchfilebetweentags-doc
Summary:        Documentation for catchfilebetweentags
Version:        svn21476.1.1

Provides:       tex-catchfilebetweentags-doc
AutoReqProv:    No

%description -n texlive-catchfilebetweentags-doc
Documentation for catchfilebetweentags

%package -n texlive-catcodes
Provides:       tex-catcodes = %{tl_version}
License:        LPPL 1.3
Summary:        Generic handling of TeX category codes
Version:        svn38859

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(actcodes.sty) = %{tl_version}, tex(catchdq.sty) = %{tl_version}
Provides:       tex(stacklet.sty) = %{tl_version}

%description -n texlive-catcodes
The bundle deals with category code switching; the packages of
the bundle should work with any TeX format (with the support of
the plainpkg package). The bundle provides: stacklet.sty, which
supports stacks that control the use of different catcodes;
actcodes.sty, which deals with active characters; and
catchdq.sty, which provides a simple quotation character
control mechanism.

%package -n texlive-catcodes-doc
Summary:        Documentation for catcodes
Version:        svn38859

Provides:       tex-catcodes-doc
AutoReqProv:    No

%description -n texlive-catcodes-doc
Documentation for catcodes

%package -n texlive-catechis
Provides:       tex-catechis = %{tl_version}
License:        LPPL
Summary:        Macros for typesetting catechisms
Version:        svn48198
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(calc.sty), tex(ifthen.sty), tex(varioref.sty)
Provides:       tex(catechis.sty) = %{tl_version}

%description -n texlive-catechis
The macros include: format for question-and-answer; comments on
answers; citations; a specialised enumerate which only operates
in the catechism parts of a document. The macros are all highly
customisable.

%package -n texlive-catechis-doc
Summary:        Documentation for catechis
Version:        svn48198
Provides:       tex-catechis-doc
AutoReqProv:    No

%description -n texlive-catechis-doc
Documentation for catechis

%package -n texlive-catoptions
Provides:       tex-catoptions = %{tl_version}
License:        LPPL 1.3
Summary:        Preserving and recalling standard catcodes
Version:        svn35069.0.2.7h

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(pdftexcmds.sty)
Provides:       tex(catoptions-guide.cfg) = %{tl_version}
Provides:       tex(catoptions.sty) = %{tl_version}

%description -n texlive-catoptions
The package changes package loading internals so that all
subsequently loaded packages can rely on normal/standard
catcodes of all ASCII characters. The package defines canonical
control sequences to represent all the visible ASCII
characters. It also provides robust option parsing mechanisms
(XDeclareOption, XExecuteOptions and XProcessOptions, which
will be used by \documentclass if the package has already been
loaded). The package also provides a range of other TeX
programming tools.

%package -n texlive-catoptions-doc
Summary:        Documentation for catoptions
Version:        svn35069.0.2.7h

Provides:       tex-catoptions-doc
AutoReqProv:    No

%description -n texlive-catoptions-doc
Documentation for catoptions

%package -n texlive-cbcoptic
Provides:       tex-cbcoptic = %{tl_version}
License:        LPPL
Summary:        Coptic fonts and LaTeX macros for general usage and for philology
Version:        svn16666.0.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(textcomp.sty)
Provides:       tex(copti.tfm) = %{tl_version}, tex(copto.tfm) = %{tl_version}
Provides:       tex(copti.pfb) = %{tl_version}, tex(copto.pfb) = %{tl_version}
Provides:       tex(coptic.sty) = %{tl_version}, tex(lcopcoptic.fd) = %{tl_version}
Provides:       tex(prnthyph.sty) = %{tl_version}

%description -n texlive-cbcoptic
CBcoptic is a bundle of files for typesetting Coptic
philological text with the proper fonts and hyphenation. The
fonts are based on, but much extend, the fonts of the original
coptic bundle. The CBcoptic bundle includes font description
files, Metafont sources and equivalent Adobe Type 1 fonts in
pfb format. The bundle also includes a package that provides
some macros of philological interest.

%package -n texlive-cbcoptic-doc
Summary:        Documentation for cbcoptic
Version:        svn16666.0.2

Provides:       tex-cbcoptic-doc
AutoReqProv:    No

%description -n texlive-cbcoptic-doc
Documentation for cbcoptic

%package -n texlive-cbfonts-fd
Provides:       tex-cbfonts-fd = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX font description files for the CB Greek fonts
Version:        svn44917
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(lgrcmr.fd) = %{tl_version}, tex(lgrcmro.fd) = %{tl_version}
Provides:       tex(lgrcmss.fd) = %{tl_version}, tex(lgrcmtt.fd) = %{tl_version}
Provides:       tex(lgrlcmss.fd) = %{tl_version}, tex(lgrlcmtt.fd) = %{tl_version}
Provides:       tex(lgrlmr.fd) = %{tl_version}, tex(lgrlmro.fd) = %{tl_version}
Provides:       tex(lgrlmss.fd) = %{tl_version}, tex(lgrlmtt.fd) = %{tl_version}

%description -n texlive-cbfonts-fd
The package provides font description files for all the many
shapes available from the cbfonts collection. The files provide
the means whereby the NFSS knows which fonts a LaTeX user is
requesting.

%package -n texlive-cbfonts-fd-doc
Summary:        Documentation for cbfonts-fd
Version:        svn44917
Provides:       tex-cbfonts-fd-doc
AutoReqProv:    No

%description -n texlive-cbfonts-fd-doc
Documentation for cbfonts-fd

%package -n texlive-cbfonts
Provides:       tex-cbfonts = %{tl_version}
License:        LPPL
Summary:        Complete set of Greek fonts
Version:        svn31624.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex-cbfonts-fd
Provides:       tex(CB.enc) = %{tl_version}, tex(gmtr.enc) = %{tl_version}
Provides:       tex(cbgreek-full.map) = %{tl_version}, tex(glic0700.tfm) = %{tl_version}
Provides:       tex(glic0800.tfm) = %{tl_version}, tex(glic1000.tfm) = %{tl_version}
Provides:       tex(glic1200.tfm) = %{tl_version}, tex(glic1382.tfm) = %{tl_version}
Provides:       tex(glic1659.tfm) = %{tl_version}, tex(glic1991.tfm) = %{tl_version}
Provides:       tex(glic2389.tfm) = %{tl_version}, tex(glic2866.tfm) = %{tl_version}
Provides:       tex(glic3440.tfm) = %{tl_version}, tex(glic4128.tfm) = %{tl_version}
Provides:       tex(glii0700.tfm) = %{tl_version}, tex(glii0800.tfm) = %{tl_version}
Provides:       tex(glii1000.tfm) = %{tl_version}, tex(glii1200.tfm) = %{tl_version}
Provides:       tex(glii1382.tfm) = %{tl_version}, tex(glii1659.tfm) = %{tl_version}
Provides:       tex(glii1991.tfm) = %{tl_version}, tex(glii2389.tfm) = %{tl_version}
Provides:       tex(glii2866.tfm) = %{tl_version}, tex(glii3440.tfm) = %{tl_version}
Provides:       tex(glii4128.tfm) = %{tl_version}, tex(glin0700.tfm) = %{tl_version}
Provides:       tex(glin0800.tfm) = %{tl_version}, tex(glin1000.tfm) = %{tl_version}
Provides:       tex(glin1200.tfm) = %{tl_version}, tex(glin1382.tfm) = %{tl_version}
Provides:       tex(glin1659.tfm) = %{tl_version}, tex(glin1991.tfm) = %{tl_version}
Provides:       tex(glin2389.tfm) = %{tl_version}, tex(glin2866.tfm) = %{tl_version}
Provides:       tex(glin3440.tfm) = %{tl_version}, tex(glin4128.tfm) = %{tl_version}
Provides:       tex(glio0700.tfm) = %{tl_version}, tex(glio0800.tfm) = %{tl_version}
Provides:       tex(glio1000.tfm) = %{tl_version}, tex(glio1200.tfm) = %{tl_version}
Provides:       tex(glio1382.tfm) = %{tl_version}, tex(glio1659.tfm) = %{tl_version}
Provides:       tex(glio1991.tfm) = %{tl_version}, tex(glio2389.tfm) = %{tl_version}
Provides:       tex(glio2866.tfm) = %{tl_version}, tex(glio3440.tfm) = %{tl_version}
Provides:       tex(glio4128.tfm) = %{tl_version}, tex(gliu0700.tfm) = %{tl_version}
Provides:       tex(gliu0800.tfm) = %{tl_version}, tex(gliu1000.tfm) = %{tl_version}
Provides:       tex(gliu1200.tfm) = %{tl_version}, tex(gliu1382.tfm) = %{tl_version}
Provides:       tex(gliu1659.tfm) = %{tl_version}, tex(gliu1991.tfm) = %{tl_version}
Provides:       tex(gliu2389.tfm) = %{tl_version}, tex(gliu2866.tfm) = %{tl_version}
Provides:       tex(gliu3440.tfm) = %{tl_version}, tex(gliu4128.tfm) = %{tl_version}
Provides:       tex(gljc0700.tfm) = %{tl_version}, tex(gljc0800.tfm) = %{tl_version}
Provides:       tex(gljc1000.tfm) = %{tl_version}, tex(gljc1200.tfm) = %{tl_version}
Provides:       tex(gljc1382.tfm) = %{tl_version}, tex(gljc1659.tfm) = %{tl_version}
Provides:       tex(gljc1991.tfm) = %{tl_version}, tex(gljc2389.tfm) = %{tl_version}
Provides:       tex(gljc2866.tfm) = %{tl_version}, tex(gljc3440.tfm) = %{tl_version}
Provides:       tex(gljc4128.tfm) = %{tl_version}, tex(gljn0700.tfm) = %{tl_version}
Provides:       tex(gljn0800.tfm) = %{tl_version}, tex(gljn1000.tfm) = %{tl_version}
Provides:       tex(gljn1200.tfm) = %{tl_version}, tex(gljn1382.tfm) = %{tl_version}
Provides:       tex(gljn1659.tfm) = %{tl_version}, tex(gljn1991.tfm) = %{tl_version}
Provides:       tex(gljn2389.tfm) = %{tl_version}, tex(gljn2866.tfm) = %{tl_version}
Provides:       tex(gljn3440.tfm) = %{tl_version}, tex(gljn4128.tfm) = %{tl_version}
Provides:       tex(gljo0700.tfm) = %{tl_version}, tex(gljo0800.tfm) = %{tl_version}
Provides:       tex(gljo1000.tfm) = %{tl_version}, tex(gljo1200.tfm) = %{tl_version}
Provides:       tex(gljo1382.tfm) = %{tl_version}, tex(gljo1659.tfm) = %{tl_version}
Provides:       tex(gljo1991.tfm) = %{tl_version}, tex(gljo2389.tfm) = %{tl_version}
Provides:       tex(gljo2866.tfm) = %{tl_version}, tex(gljo3440.tfm) = %{tl_version}
Provides:       tex(gljo4128.tfm) = %{tl_version}, tex(glmc0700.tfm) = %{tl_version}
Provides:       tex(glmc0800.tfm) = %{tl_version}, tex(glmc1000.tfm) = %{tl_version}
Provides:       tex(glmc1200.tfm) = %{tl_version}, tex(glmc1382.tfm) = %{tl_version}
Provides:       tex(glmc1659.tfm) = %{tl_version}, tex(glmc1991.tfm) = %{tl_version}
Provides:       tex(glmc2389.tfm) = %{tl_version}, tex(glmc2866.tfm) = %{tl_version}
Provides:       tex(glmc3440.tfm) = %{tl_version}, tex(glmc4128.tfm) = %{tl_version}
Provides:       tex(glmi0700.tfm) = %{tl_version}, tex(glmi0800.tfm) = %{tl_version}
Provides:       tex(glmi1000.tfm) = %{tl_version}, tex(glmi1200.tfm) = %{tl_version}
Provides:       tex(glmi1382.tfm) = %{tl_version}, tex(glmi1659.tfm) = %{tl_version}
Provides:       tex(glmi1991.tfm) = %{tl_version}, tex(glmi2389.tfm) = %{tl_version}
Provides:       tex(glmi2866.tfm) = %{tl_version}, tex(glmi3440.tfm) = %{tl_version}
Provides:       tex(glmi4128.tfm) = %{tl_version}, tex(glmn0700.tfm) = %{tl_version}
Provides:       tex(glmn0800.tfm) = %{tl_version}, tex(glmn1000.tfm) = %{tl_version}
Provides:       tex(glmn1200.tfm) = %{tl_version}, tex(glmn1382.tfm) = %{tl_version}
Provides:       tex(glmn1659.tfm) = %{tl_version}, tex(glmn1991.tfm) = %{tl_version}
Provides:       tex(glmn2389.tfm) = %{tl_version}, tex(glmn2866.tfm) = %{tl_version}
Provides:       tex(glmn3440.tfm) = %{tl_version}, tex(glmn4128.tfm) = %{tl_version}
Provides:       tex(glmo0700.tfm) = %{tl_version}, tex(glmo0800.tfm) = %{tl_version}
Provides:       tex(glmo1000.tfm) = %{tl_version}, tex(glmo1200.tfm) = %{tl_version}
Provides:       tex(glmo1382.tfm) = %{tl_version}, tex(glmo1659.tfm) = %{tl_version}
Provides:       tex(glmo1991.tfm) = %{tl_version}, tex(glmo2389.tfm) = %{tl_version}
Provides:       tex(glmo2866.tfm) = %{tl_version}, tex(glmo3440.tfm) = %{tl_version}
Provides:       tex(glmo4128.tfm) = %{tl_version}, tex(glmu0700.tfm) = %{tl_version}
Provides:       tex(glmu0800.tfm) = %{tl_version}, tex(glmu1000.tfm) = %{tl_version}
Provides:       tex(glmu1200.tfm) = %{tl_version}, tex(glmu1382.tfm) = %{tl_version}
Provides:       tex(glmu1659.tfm) = %{tl_version}, tex(glmu1991.tfm) = %{tl_version}
Provides:       tex(glmu2389.tfm) = %{tl_version}, tex(glmu2866.tfm) = %{tl_version}
Provides:       tex(glmu3440.tfm) = %{tl_version}, tex(glmu4128.tfm) = %{tl_version}
Provides:       tex(gltc0700.tfm) = %{tl_version}, tex(gltc0800.tfm) = %{tl_version}
Provides:       tex(gltc1000.tfm) = %{tl_version}, tex(gltc1200.tfm) = %{tl_version}
Provides:       tex(gltc1382.tfm) = %{tl_version}, tex(gltc1659.tfm) = %{tl_version}
Provides:       tex(gltc1991.tfm) = %{tl_version}, tex(gltc2389.tfm) = %{tl_version}
Provides:       tex(gltc2866.tfm) = %{tl_version}, tex(gltc3440.tfm) = %{tl_version}
Provides:       tex(gltc4128.tfm) = %{tl_version}, tex(gltn0700.tfm) = %{tl_version}
Provides:       tex(gltn0800.tfm) = %{tl_version}, tex(gltn1000.tfm) = %{tl_version}
Provides:       tex(gltn1200.tfm) = %{tl_version}, tex(gltn1382.tfm) = %{tl_version}
Provides:       tex(gltn1659.tfm) = %{tl_version}, tex(gltn1991.tfm) = %{tl_version}
Provides:       tex(gltn2389.tfm) = %{tl_version}, tex(gltn2866.tfm) = %{tl_version}
Provides:       tex(gltn3440.tfm) = %{tl_version}, tex(gltn4128.tfm) = %{tl_version}
Provides:       tex(glto0700.tfm) = %{tl_version}, tex(glto0800.tfm) = %{tl_version}
Provides:       tex(glto1000.tfm) = %{tl_version}, tex(glto1200.tfm) = %{tl_version}
Provides:       tex(glto1382.tfm) = %{tl_version}, tex(glto1659.tfm) = %{tl_version}
Provides:       tex(glto1991.tfm) = %{tl_version}, tex(glto2389.tfm) = %{tl_version}
Provides:       tex(glto2866.tfm) = %{tl_version}, tex(glto3440.tfm) = %{tl_version}
Provides:       tex(glto4128.tfm) = %{tl_version}, tex(glwc0700.tfm) = %{tl_version}
Provides:       tex(glwc0800.tfm) = %{tl_version}, tex(glwc1000.tfm) = %{tl_version}
Provides:       tex(glwc1200.tfm) = %{tl_version}, tex(glwc1382.tfm) = %{tl_version}
Provides:       tex(glwc1659.tfm) = %{tl_version}, tex(glwc1991.tfm) = %{tl_version}
Provides:       tex(glwc2389.tfm) = %{tl_version}, tex(glwc2866.tfm) = %{tl_version}
Provides:       tex(glwc3440.tfm) = %{tl_version}, tex(glwc4128.tfm) = %{tl_version}
Provides:       tex(glwi0700.tfm) = %{tl_version}, tex(glwi0800.tfm) = %{tl_version}
Provides:       tex(glwi1000.tfm) = %{tl_version}, tex(glwi1200.tfm) = %{tl_version}
Provides:       tex(glwi1382.tfm) = %{tl_version}, tex(glwi1659.tfm) = %{tl_version}
Provides:       tex(glwi1991.tfm) = %{tl_version}, tex(glwi2389.tfm) = %{tl_version}
Provides:       tex(glwi2866.tfm) = %{tl_version}, tex(glwi3440.tfm) = %{tl_version}
Provides:       tex(glwi4128.tfm) = %{tl_version}, tex(glwn0700.tfm) = %{tl_version}
Provides:       tex(glwn0800.tfm) = %{tl_version}, tex(glwn1000.tfm) = %{tl_version}
Provides:       tex(glwn1200.tfm) = %{tl_version}, tex(glwn1382.tfm) = %{tl_version}
Provides:       tex(glwn1659.tfm) = %{tl_version}, tex(glwn1991.tfm) = %{tl_version}
Provides:       tex(glwn2389.tfm) = %{tl_version}, tex(glwn2866.tfm) = %{tl_version}
Provides:       tex(glwn3440.tfm) = %{tl_version}, tex(glwn4128.tfm) = %{tl_version}
Provides:       tex(glwo0700.tfm) = %{tl_version}, tex(glwo0800.tfm) = %{tl_version}
Provides:       tex(glwo1000.tfm) = %{tl_version}, tex(glwo1200.tfm) = %{tl_version}
Provides:       tex(glwo1382.tfm) = %{tl_version}, tex(glwo1659.tfm) = %{tl_version}
Provides:       tex(glwo1991.tfm) = %{tl_version}, tex(glwo2389.tfm) = %{tl_version}
Provides:       tex(glwo2866.tfm) = %{tl_version}, tex(glwo3440.tfm) = %{tl_version}
Provides:       tex(glwo4128.tfm) = %{tl_version}, tex(glwu0700.tfm) = %{tl_version}
Provides:       tex(glwu0800.tfm) = %{tl_version}, tex(glwu1000.tfm) = %{tl_version}
Provides:       tex(glwu1200.tfm) = %{tl_version}, tex(glwu1382.tfm) = %{tl_version}
Provides:       tex(glwu1659.tfm) = %{tl_version}, tex(glwu1991.tfm) = %{tl_version}
Provides:       tex(glwu2389.tfm) = %{tl_version}, tex(glwu2866.tfm) = %{tl_version}
Provides:       tex(glwu3440.tfm) = %{tl_version}, tex(glwu4128.tfm) = %{tl_version}
Provides:       tex(glxc0700.tfm) = %{tl_version}, tex(glxc0800.tfm) = %{tl_version}
Provides:       tex(glxc1000.tfm) = %{tl_version}, tex(glxc1200.tfm) = %{tl_version}
Provides:       tex(glxc1382.tfm) = %{tl_version}, tex(glxc1659.tfm) = %{tl_version}
Provides:       tex(glxc1991.tfm) = %{tl_version}, tex(glxc2389.tfm) = %{tl_version}
Provides:       tex(glxc2866.tfm) = %{tl_version}, tex(glxc3440.tfm) = %{tl_version}
Provides:       tex(glxc4128.tfm) = %{tl_version}, tex(glxi0700.tfm) = %{tl_version}
Provides:       tex(glxi0800.tfm) = %{tl_version}, tex(glxi1000.tfm) = %{tl_version}
Provides:       tex(glxi1200.tfm) = %{tl_version}, tex(glxi1382.tfm) = %{tl_version}
Provides:       tex(glxi1659.tfm) = %{tl_version}, tex(glxi1991.tfm) = %{tl_version}
Provides:       tex(glxi2389.tfm) = %{tl_version}, tex(glxi2866.tfm) = %{tl_version}
Provides:       tex(glxi3440.tfm) = %{tl_version}, tex(glxi4128.tfm) = %{tl_version}
Provides:       tex(glxn0700.tfm) = %{tl_version}, tex(glxn0800.tfm) = %{tl_version}
Provides:       tex(glxn1000.tfm) = %{tl_version}, tex(glxn1200.tfm) = %{tl_version}
Provides:       tex(glxn1382.tfm) = %{tl_version}, tex(glxn1659.tfm) = %{tl_version}
Provides:       tex(glxn1991.tfm) = %{tl_version}, tex(glxn2389.tfm) = %{tl_version}
Provides:       tex(glxn2866.tfm) = %{tl_version}, tex(glxn3440.tfm) = %{tl_version}
Provides:       tex(glxn4128.tfm) = %{tl_version}, tex(glxo0700.tfm) = %{tl_version}
Provides:       tex(glxo0800.tfm) = %{tl_version}, tex(glxo1000.tfm) = %{tl_version}
Provides:       tex(glxo1200.tfm) = %{tl_version}, tex(glxo1382.tfm) = %{tl_version}
Provides:       tex(glxo1659.tfm) = %{tl_version}, tex(glxo1991.tfm) = %{tl_version}
Provides:       tex(glxo2389.tfm) = %{tl_version}, tex(glxo2866.tfm) = %{tl_version}
Provides:       tex(glxo3440.tfm) = %{tl_version}, tex(glxo4128.tfm) = %{tl_version}
Provides:       tex(glxu0700.tfm) = %{tl_version}, tex(glxu0800.tfm) = %{tl_version}
Provides:       tex(glxu1000.tfm) = %{tl_version}, tex(glxu1200.tfm) = %{tl_version}
Provides:       tex(glxu1382.tfm) = %{tl_version}, tex(glxu1659.tfm) = %{tl_version}
Provides:       tex(glxu1991.tfm) = %{tl_version}, tex(glxu2389.tfm) = %{tl_version}
Provides:       tex(glxu2866.tfm) = %{tl_version}, tex(glxu3440.tfm) = %{tl_version}
Provides:       tex(glxu4128.tfm) = %{tl_version}, tex(gmmn0500.tfm) = %{tl_version}
Provides:       tex(gmmn0600.tfm) = %{tl_version}, tex(gmmn0700.tfm) = %{tl_version}
Provides:       tex(gmmn0800.tfm) = %{tl_version}, tex(gmmn0900.tfm) = %{tl_version}
Provides:       tex(gmmn1000.tfm) = %{tl_version}, tex(gmmn1095.tfm) = %{tl_version}
Provides:       tex(gmmn1200.tfm) = %{tl_version}, tex(gmmn1440.tfm) = %{tl_version}
Provides:       tex(gmmn1728.tfm) = %{tl_version}, tex(gmmn2074.tfm) = %{tl_version}
Provides:       tex(gmmn2488.tfm) = %{tl_version}, tex(gmmn2986.tfm) = %{tl_version}
Provides:       tex(gmmn3583.tfm) = %{tl_version}, tex(gmmo0500.tfm) = %{tl_version}
Provides:       tex(gmmo0600.tfm) = %{tl_version}, tex(gmmo0700.tfm) = %{tl_version}
Provides:       tex(gmmo0800.tfm) = %{tl_version}, tex(gmmo0900.tfm) = %{tl_version}
Provides:       tex(gmmo1000.tfm) = %{tl_version}, tex(gmmo1095.tfm) = %{tl_version}
Provides:       tex(gmmo1200.tfm) = %{tl_version}, tex(gmmo1440.tfm) = %{tl_version}
Provides:       tex(gmmo1728.tfm) = %{tl_version}, tex(gmmo2074.tfm) = %{tl_version}
Provides:       tex(gmmo2488.tfm) = %{tl_version}, tex(gmmo2986.tfm) = %{tl_version}
Provides:       tex(gmmo3583.tfm) = %{tl_version}, tex(gmtr0500.tfm) = %{tl_version}
Provides:       tex(gmtr0600.tfm) = %{tl_version}, tex(gmtr0700.tfm) = %{tl_version}
Provides:       tex(gmtr0800.tfm) = %{tl_version}, tex(gmtr0900.tfm) = %{tl_version}
Provides:       tex(gmtr1000.tfm) = %{tl_version}, tex(gmtr1095.tfm) = %{tl_version}
Provides:       tex(gmtr1200.tfm) = %{tl_version}, tex(gmtr1440.tfm) = %{tl_version}
Provides:       tex(gmtr1728.tfm) = %{tl_version}, tex(gmtr2074.tfm) = %{tl_version}
Provides:       tex(gmtr2488.tfm) = %{tl_version}, tex(gmtr2986.tfm) = %{tl_version}
Provides:       tex(gmtr3583.tfm) = %{tl_version}, tex(gmxn0500.tfm) = %{tl_version}
Provides:       tex(gmxn0600.tfm) = %{tl_version}, tex(gmxn0700.tfm) = %{tl_version}
Provides:       tex(gmxn0800.tfm) = %{tl_version}, tex(gmxn0900.tfm) = %{tl_version}
Provides:       tex(gmxn1000.tfm) = %{tl_version}, tex(gmxn1095.tfm) = %{tl_version}
Provides:       tex(gmxn1200.tfm) = %{tl_version}, tex(gmxn1440.tfm) = %{tl_version}
Provides:       tex(gmxn1728.tfm) = %{tl_version}, tex(gmxn2074.tfm) = %{tl_version}
Provides:       tex(gmxn2488.tfm) = %{tl_version}, tex(gmxn2986.tfm) = %{tl_version}
Provides:       tex(gmxn3583.tfm) = %{tl_version}, tex(gmxo0500.tfm) = %{tl_version}
Provides:       tex(gmxo0600.tfm) = %{tl_version}, tex(gmxo0700.tfm) = %{tl_version}
Provides:       tex(gmxo0800.tfm) = %{tl_version}, tex(gmxo0900.tfm) = %{tl_version}
Provides:       tex(gmxo1000.tfm) = %{tl_version}, tex(gmxo1095.tfm) = %{tl_version}
Provides:       tex(gmxo1200.tfm) = %{tl_version}, tex(gmxo1440.tfm) = %{tl_version}
Provides:       tex(gmxo1728.tfm) = %{tl_version}, tex(gmxo2074.tfm) = %{tl_version}
Provides:       tex(gmxo2488.tfm) = %{tl_version}, tex(gmxo2986.tfm) = %{tl_version}
Provides:       tex(gmxo3583.tfm) = %{tl_version}, tex(gomc0500.tfm) = %{tl_version}
Provides:       tex(gomc0600.tfm) = %{tl_version}, tex(gomc0700.tfm) = %{tl_version}
Provides:       tex(gomc0800.tfm) = %{tl_version}, tex(gomc0900.tfm) = %{tl_version}
Provides:       tex(gomc1000.tfm) = %{tl_version}, tex(gomc1095.tfm) = %{tl_version}
Provides:       tex(gomc1200.tfm) = %{tl_version}, tex(gomc1440.tfm) = %{tl_version}
Provides:       tex(gomc1728.tfm) = %{tl_version}, tex(gomc2074.tfm) = %{tl_version}
Provides:       tex(gomc2488.tfm) = %{tl_version}, tex(gomc2986.tfm) = %{tl_version}
Provides:       tex(gomc3583.tfm) = %{tl_version}, tex(gomi0500.tfm) = %{tl_version}
Provides:       tex(gomi0600.tfm) = %{tl_version}, tex(gomi0700.tfm) = %{tl_version}
Provides:       tex(gomi0800.tfm) = %{tl_version}, tex(gomi0900.tfm) = %{tl_version}
Provides:       tex(gomi1000.tfm) = %{tl_version}, tex(gomi1095.tfm) = %{tl_version}
Provides:       tex(gomi1200.tfm) = %{tl_version}, tex(gomi1440.tfm) = %{tl_version}
Provides:       tex(gomi1728.tfm) = %{tl_version}, tex(gomi2074.tfm) = %{tl_version}
Provides:       tex(gomi2488.tfm) = %{tl_version}, tex(gomi2986.tfm) = %{tl_version}
Provides:       tex(gomi3583.tfm) = %{tl_version}, tex(gomn0500.tfm) = %{tl_version}
Provides:       tex(gomn0600.tfm) = %{tl_version}, tex(gomn0700.tfm) = %{tl_version}
Provides:       tex(gomn0800.tfm) = %{tl_version}, tex(gomn0900.tfm) = %{tl_version}
Provides:       tex(gomn1000.tfm) = %{tl_version}, tex(gomn1095.tfm) = %{tl_version}
Provides:       tex(gomn1200.tfm) = %{tl_version}, tex(gomn1440.tfm) = %{tl_version}
Provides:       tex(gomn1728.tfm) = %{tl_version}, tex(gomn2074.tfm) = %{tl_version}
Provides:       tex(gomn2488.tfm) = %{tl_version}, tex(gomn2986.tfm) = %{tl_version}
Provides:       tex(gomn3583.tfm) = %{tl_version}, tex(gomo0500.tfm) = %{tl_version}
Provides:       tex(gomo0600.tfm) = %{tl_version}, tex(gomo0700.tfm) = %{tl_version}
Provides:       tex(gomo0800.tfm) = %{tl_version}, tex(gomo0900.tfm) = %{tl_version}
Provides:       tex(gomo1000.tfm) = %{tl_version}, tex(gomo1095.tfm) = %{tl_version}
Provides:       tex(gomo1200.tfm) = %{tl_version}, tex(gomo1440.tfm) = %{tl_version}
Provides:       tex(gomo1728.tfm) = %{tl_version}, tex(gomo2074.tfm) = %{tl_version}
Provides:       tex(gomo2488.tfm) = %{tl_version}, tex(gomo2986.tfm) = %{tl_version}
Provides:       tex(gomo3583.tfm) = %{tl_version}, tex(gomu0500.tfm) = %{tl_version}
Provides:       tex(gomu0600.tfm) = %{tl_version}, tex(gomu0700.tfm) = %{tl_version}
Provides:       tex(gomu0800.tfm) = %{tl_version}, tex(gomu0900.tfm) = %{tl_version}
Provides:       tex(gomu1000.tfm) = %{tl_version}, tex(gomu1095.tfm) = %{tl_version}
Provides:       tex(gomu1200.tfm) = %{tl_version}, tex(gomu1440.tfm) = %{tl_version}
Provides:       tex(gomu1728.tfm) = %{tl_version}, tex(gomu2074.tfm) = %{tl_version}
Provides:       tex(gomu2488.tfm) = %{tl_version}, tex(gomu2986.tfm) = %{tl_version}
Provides:       tex(gomu3583.tfm) = %{tl_version}, tex(goxc0500.tfm) = %{tl_version}
Provides:       tex(goxc0600.tfm) = %{tl_version}, tex(goxc0700.tfm) = %{tl_version}
Provides:       tex(goxc0800.tfm) = %{tl_version}, tex(goxc0900.tfm) = %{tl_version}
Provides:       tex(goxc1000.tfm) = %{tl_version}, tex(goxc1095.tfm) = %{tl_version}
Provides:       tex(goxc1200.tfm) = %{tl_version}, tex(goxc1440.tfm) = %{tl_version}
Provides:       tex(goxc1728.tfm) = %{tl_version}, tex(goxc2074.tfm) = %{tl_version}
Provides:       tex(goxc2488.tfm) = %{tl_version}, tex(goxc2986.tfm) = %{tl_version}
Provides:       tex(goxc3583.tfm) = %{tl_version}, tex(goxi0500.tfm) = %{tl_version}
Provides:       tex(goxi0600.tfm) = %{tl_version}, tex(goxi0700.tfm) = %{tl_version}
Provides:       tex(goxi0800.tfm) = %{tl_version}, tex(goxi0900.tfm) = %{tl_version}
Provides:       tex(goxi1000.tfm) = %{tl_version}, tex(goxi1095.tfm) = %{tl_version}
Provides:       tex(goxi1200.tfm) = %{tl_version}, tex(goxi1440.tfm) = %{tl_version}
Provides:       tex(goxi1728.tfm) = %{tl_version}, tex(goxi2074.tfm) = %{tl_version}
Provides:       tex(goxi2488.tfm) = %{tl_version}, tex(goxi2986.tfm) = %{tl_version}
Provides:       tex(goxi3583.tfm) = %{tl_version}, tex(goxn0500.tfm) = %{tl_version}
Provides:       tex(goxn0600.tfm) = %{tl_version}, tex(goxn0700.tfm) = %{tl_version}
Provides:       tex(goxn0800.tfm) = %{tl_version}, tex(goxn0900.tfm) = %{tl_version}
Provides:       tex(goxn1000.tfm) = %{tl_version}, tex(goxn1095.tfm) = %{tl_version}
Provides:       tex(goxn1200.tfm) = %{tl_version}, tex(goxn1440.tfm) = %{tl_version}
Provides:       tex(goxn1728.tfm) = %{tl_version}, tex(goxn2074.tfm) = %{tl_version}
Provides:       tex(goxn2488.tfm) = %{tl_version}, tex(goxn2986.tfm) = %{tl_version}
Provides:       tex(goxn3583.tfm) = %{tl_version}, tex(goxo0500.tfm) = %{tl_version}
Provides:       tex(goxo0600.tfm) = %{tl_version}, tex(goxo0700.tfm) = %{tl_version}
Provides:       tex(goxo0800.tfm) = %{tl_version}, tex(goxo0900.tfm) = %{tl_version}
Provides:       tex(goxo1000.tfm) = %{tl_version}, tex(goxo1095.tfm) = %{tl_version}
Provides:       tex(goxo1200.tfm) = %{tl_version}, tex(goxo1440.tfm) = %{tl_version}
Provides:       tex(goxo1728.tfm) = %{tl_version}, tex(goxo2074.tfm) = %{tl_version}
Provides:       tex(goxo2488.tfm) = %{tl_version}, tex(goxo2986.tfm) = %{tl_version}
Provides:       tex(goxo3583.tfm) = %{tl_version}, tex(goxu0500.tfm) = %{tl_version}
Provides:       tex(goxu0600.tfm) = %{tl_version}, tex(goxu0700.tfm) = %{tl_version}
Provides:       tex(goxu0800.tfm) = %{tl_version}, tex(goxu0900.tfm) = %{tl_version}
Provides:       tex(goxu1000.tfm) = %{tl_version}, tex(goxu1095.tfm) = %{tl_version}
Provides:       tex(goxu1200.tfm) = %{tl_version}, tex(goxu1440.tfm) = %{tl_version}
Provides:       tex(goxu1728.tfm) = %{tl_version}, tex(goxu2074.tfm) = %{tl_version}
Provides:       tex(goxu2488.tfm) = %{tl_version}, tex(goxu2986.tfm) = %{tl_version}
Provides:       tex(goxu3583.tfm) = %{tl_version}, tex(grbl0500.tfm) = %{tl_version}
Provides:       tex(grbl0600.tfm) = %{tl_version}, tex(grbl0700.tfm) = %{tl_version}
Provides:       tex(grbl0800.tfm) = %{tl_version}, tex(grbl0900.tfm) = %{tl_version}
Provides:       tex(grbl1000.tfm) = %{tl_version}, tex(grbl1095.tfm) = %{tl_version}
Provides:       tex(grbl1200.tfm) = %{tl_version}, tex(grbl1440.tfm) = %{tl_version}
Provides:       tex(grbl1728.tfm) = %{tl_version}, tex(grbl2074.tfm) = %{tl_version}
Provides:       tex(grbl2488.tfm) = %{tl_version}, tex(grbl2986.tfm) = %{tl_version}
Provides:       tex(grbl3583.tfm) = %{tl_version}, tex(grmc0500.tfm) = %{tl_version}
Provides:       tex(grmc0600.tfm) = %{tl_version}, tex(grmc0700.tfm) = %{tl_version}
Provides:       tex(grmc0800.tfm) = %{tl_version}, tex(grmc0900.tfm) = %{tl_version}
Provides:       tex(grmc1000.tfm) = %{tl_version}, tex(grmc1095.tfm) = %{tl_version}
Provides:       tex(grmc1200.tfm) = %{tl_version}, tex(grmc1440.tfm) = %{tl_version}
Provides:       tex(grmc1728.tfm) = %{tl_version}, tex(grmc2074.tfm) = %{tl_version}
Provides:       tex(grmc2488.tfm) = %{tl_version}, tex(grmc2986.tfm) = %{tl_version}
Provides:       tex(grmc3583.tfm) = %{tl_version}, tex(grmi0500.tfm) = %{tl_version}
Provides:       tex(grmi0600.tfm) = %{tl_version}, tex(grmi0700.tfm) = %{tl_version}
Provides:       tex(grmi0800.tfm) = %{tl_version}, tex(grmi0900.tfm) = %{tl_version}
Provides:       tex(grmi1000.tfm) = %{tl_version}, tex(grmi1095.tfm) = %{tl_version}
Provides:       tex(grmi1200.tfm) = %{tl_version}, tex(grmi1440.tfm) = %{tl_version}
Provides:       tex(grmi1728.tfm) = %{tl_version}, tex(grmi2074.tfm) = %{tl_version}
Provides:       tex(grmi2488.tfm) = %{tl_version}, tex(grmi2986.tfm) = %{tl_version}
Provides:       tex(grmi3583.tfm) = %{tl_version}, tex(grml0500.tfm) = %{tl_version}
Provides:       tex(grml0600.tfm) = %{tl_version}, tex(grml0700.tfm) = %{tl_version}
Provides:       tex(grml0800.tfm) = %{tl_version}, tex(grml0900.tfm) = %{tl_version}
Provides:       tex(grml1000.tfm) = %{tl_version}, tex(grml1095.tfm) = %{tl_version}
Provides:       tex(grml1200.tfm) = %{tl_version}, tex(grml1440.tfm) = %{tl_version}
Provides:       tex(grml1728.tfm) = %{tl_version}, tex(grml2074.tfm) = %{tl_version}
Provides:       tex(grml2488.tfm) = %{tl_version}, tex(grml2986.tfm) = %{tl_version}
Provides:       tex(grml3583.tfm) = %{tl_version}, tex(grmn0500.tfm) = %{tl_version}
Provides:       tex(grmn0600.tfm) = %{tl_version}, tex(grmn0700.tfm) = %{tl_version}
Provides:       tex(grmn0800.tfm) = %{tl_version}, tex(grmn0900.tfm) = %{tl_version}
Provides:       tex(grmn1000.tfm) = %{tl_version}, tex(grmn1095.tfm) = %{tl_version}
Provides:       tex(grmn1200.tfm) = %{tl_version}, tex(grmn1440.tfm) = %{tl_version}
Provides:       tex(grmn1728.tfm) = %{tl_version}, tex(grmn2074.tfm) = %{tl_version}
Provides:       tex(grmn2488.tfm) = %{tl_version}, tex(grmn2986.tfm) = %{tl_version}
Provides:       tex(grmn3583.tfm) = %{tl_version}, tex(grmo0500.tfm) = %{tl_version}
Provides:       tex(grmo0600.tfm) = %{tl_version}, tex(grmo0700.tfm) = %{tl_version}
Provides:       tex(grmo0800.tfm) = %{tl_version}, tex(grmo0900.tfm) = %{tl_version}
Provides:       tex(grmo1000.tfm) = %{tl_version}, tex(grmo1095.tfm) = %{tl_version}
Provides:       tex(grmo1200.tfm) = %{tl_version}, tex(grmo1440.tfm) = %{tl_version}
Provides:       tex(grmo1728.tfm) = %{tl_version}, tex(grmo2074.tfm) = %{tl_version}
Provides:       tex(grmo2488.tfm) = %{tl_version}, tex(grmo2986.tfm) = %{tl_version}
Provides:       tex(grmo3583.tfm) = %{tl_version}, tex(grmu0500.tfm) = %{tl_version}
Provides:       tex(grmu0600.tfm) = %{tl_version}, tex(grmu0700.tfm) = %{tl_version}
Provides:       tex(grmu0800.tfm) = %{tl_version}, tex(grmu0900.tfm) = %{tl_version}
Provides:       tex(grmu1000.tfm) = %{tl_version}, tex(grmu1095.tfm) = %{tl_version}
Provides:       tex(grmu1200.tfm) = %{tl_version}, tex(grmu1440.tfm) = %{tl_version}
Provides:       tex(grmu1728.tfm) = %{tl_version}, tex(grmu2074.tfm) = %{tl_version}
Provides:       tex(grmu2488.tfm) = %{tl_version}, tex(grmu2986.tfm) = %{tl_version}
Provides:       tex(grmu3583.tfm) = %{tl_version}, tex(grxc0500.tfm) = %{tl_version}
Provides:       tex(grxc0600.tfm) = %{tl_version}, tex(grxc0700.tfm) = %{tl_version}
Provides:       tex(grxc0800.tfm) = %{tl_version}, tex(grxc0900.tfm) = %{tl_version}
Provides:       tex(grxc1000.tfm) = %{tl_version}, tex(grxc1095.tfm) = %{tl_version}
Provides:       tex(grxc1200.tfm) = %{tl_version}, tex(grxc1440.tfm) = %{tl_version}
Provides:       tex(grxc1728.tfm) = %{tl_version}, tex(grxc2074.tfm) = %{tl_version}
Provides:       tex(grxc2488.tfm) = %{tl_version}, tex(grxc2986.tfm) = %{tl_version}
Provides:       tex(grxc3583.tfm) = %{tl_version}, tex(grxi0500.tfm) = %{tl_version}
Provides:       tex(grxi0600.tfm) = %{tl_version}, tex(grxi0700.tfm) = %{tl_version}
Provides:       tex(grxi0800.tfm) = %{tl_version}, tex(grxi0900.tfm) = %{tl_version}
Provides:       tex(grxi1000.tfm) = %{tl_version}, tex(grxi1095.tfm) = %{tl_version}
Provides:       tex(grxi1200.tfm) = %{tl_version}, tex(grxi1440.tfm) = %{tl_version}
Provides:       tex(grxi1728.tfm) = %{tl_version}, tex(grxi2074.tfm) = %{tl_version}
Provides:       tex(grxi2488.tfm) = %{tl_version}, tex(grxi2986.tfm) = %{tl_version}
Provides:       tex(grxi3583.tfm) = %{tl_version}, tex(grxl0500.tfm) = %{tl_version}
Provides:       tex(grxl0600.tfm) = %{tl_version}, tex(grxl0700.tfm) = %{tl_version}
Provides:       tex(grxl0800.tfm) = %{tl_version}, tex(grxl0900.tfm) = %{tl_version}
Provides:       tex(grxl1000.tfm) = %{tl_version}, tex(grxl1095.tfm) = %{tl_version}
Provides:       tex(grxl1200.tfm) = %{tl_version}, tex(grxl1440.tfm) = %{tl_version}
Provides:       tex(grxl1728.tfm) = %{tl_version}, tex(grxl2074.tfm) = %{tl_version}
Provides:       tex(grxl2488.tfm) = %{tl_version}, tex(grxl2986.tfm) = %{tl_version}
Provides:       tex(grxl3583.tfm) = %{tl_version}, tex(grxn0500.tfm) = %{tl_version}
Provides:       tex(grxn0600.tfm) = %{tl_version}, tex(grxn0700.tfm) = %{tl_version}
Provides:       tex(grxn0800.tfm) = %{tl_version}, tex(grxn0900.tfm) = %{tl_version}
Provides:       tex(grxn1000.tfm) = %{tl_version}, tex(grxn1095.tfm) = %{tl_version}
Provides:       tex(grxn1200.tfm) = %{tl_version}, tex(grxn1440.tfm) = %{tl_version}
Provides:       tex(grxn1728.tfm) = %{tl_version}, tex(grxn2074.tfm) = %{tl_version}
Provides:       tex(grxn2488.tfm) = %{tl_version}, tex(grxn2986.tfm) = %{tl_version}
Provides:       tex(grxn3583.tfm) = %{tl_version}, tex(grxo0500.tfm) = %{tl_version}
Provides:       tex(grxo0600.tfm) = %{tl_version}, tex(grxo0700.tfm) = %{tl_version}
Provides:       tex(grxo0800.tfm) = %{tl_version}, tex(grxo0900.tfm) = %{tl_version}
Provides:       tex(grxo1000.tfm) = %{tl_version}, tex(grxo1095.tfm) = %{tl_version}
Provides:       tex(grxo1200.tfm) = %{tl_version}, tex(grxo1440.tfm) = %{tl_version}
Provides:       tex(grxo1728.tfm) = %{tl_version}, tex(grxo2074.tfm) = %{tl_version}
Provides:       tex(grxo2488.tfm) = %{tl_version}, tex(grxo2986.tfm) = %{tl_version}
Provides:       tex(grxo3583.tfm) = %{tl_version}, tex(grxu0500.tfm) = %{tl_version}
Provides:       tex(grxu0600.tfm) = %{tl_version}, tex(grxu0700.tfm) = %{tl_version}
Provides:       tex(grxu0800.tfm) = %{tl_version}, tex(grxu0900.tfm) = %{tl_version}
Provides:       tex(grxu1000.tfm) = %{tl_version}, tex(grxu1095.tfm) = %{tl_version}
Provides:       tex(grxu1200.tfm) = %{tl_version}, tex(grxu1440.tfm) = %{tl_version}
Provides:       tex(grxu1728.tfm) = %{tl_version}, tex(grxu2074.tfm) = %{tl_version}
Provides:       tex(grxu2488.tfm) = %{tl_version}, tex(grxu2986.tfm) = %{tl_version}
Provides:       tex(grxu3583.tfm) = %{tl_version}, tex(gsma0500.tfm) = %{tl_version}
Provides:       tex(gsma0600.tfm) = %{tl_version}, tex(gsma0700.tfm) = %{tl_version}
Provides:       tex(gsma0800.tfm) = %{tl_version}, tex(gsma0900.tfm) = %{tl_version}
Provides:       tex(gsma1000.tfm) = %{tl_version}, tex(gsma1095.tfm) = %{tl_version}
Provides:       tex(gsma1200.tfm) = %{tl_version}, tex(gsma1440.tfm) = %{tl_version}
Provides:       tex(gsma1728.tfm) = %{tl_version}, tex(gsma2074.tfm) = %{tl_version}
Provides:       tex(gsma2488.tfm) = %{tl_version}, tex(gsma2986.tfm) = %{tl_version}
Provides:       tex(gsma3583.tfm) = %{tl_version}, tex(gsmc0500.tfm) = %{tl_version}
Provides:       tex(gsmc0600.tfm) = %{tl_version}, tex(gsmc0700.tfm) = %{tl_version}
Provides:       tex(gsmc0800.tfm) = %{tl_version}, tex(gsmc0900.tfm) = %{tl_version}
Provides:       tex(gsmc1000.tfm) = %{tl_version}, tex(gsmc1095.tfm) = %{tl_version}
Provides:       tex(gsmc1200.tfm) = %{tl_version}, tex(gsmc1440.tfm) = %{tl_version}
Provides:       tex(gsmc1728.tfm) = %{tl_version}, tex(gsmc2074.tfm) = %{tl_version}
Provides:       tex(gsmc2488.tfm) = %{tl_version}, tex(gsmc2986.tfm) = %{tl_version}
Provides:       tex(gsmc3583.tfm) = %{tl_version}, tex(gsme0500.tfm) = %{tl_version}
Provides:       tex(gsme0600.tfm) = %{tl_version}, tex(gsme0700.tfm) = %{tl_version}
Provides:       tex(gsme0800.tfm) = %{tl_version}, tex(gsme0900.tfm) = %{tl_version}
Provides:       tex(gsme1000.tfm) = %{tl_version}, tex(gsme1095.tfm) = %{tl_version}
Provides:       tex(gsme1200.tfm) = %{tl_version}, tex(gsme1440.tfm) = %{tl_version}
Provides:       tex(gsme1728.tfm) = %{tl_version}, tex(gsme2074.tfm) = %{tl_version}
Provides:       tex(gsme2488.tfm) = %{tl_version}, tex(gsme2986.tfm) = %{tl_version}
Provides:       tex(gsme3583.tfm) = %{tl_version}, tex(gsmi0500.tfm) = %{tl_version}
Provides:       tex(gsmi0600.tfm) = %{tl_version}, tex(gsmi0700.tfm) = %{tl_version}
Provides:       tex(gsmi0800.tfm) = %{tl_version}, tex(gsmi0900.tfm) = %{tl_version}
Provides:       tex(gsmi1000.tfm) = %{tl_version}, tex(gsmi1095.tfm) = %{tl_version}
Provides:       tex(gsmi1200.tfm) = %{tl_version}, tex(gsmi1440.tfm) = %{tl_version}
Provides:       tex(gsmi1728.tfm) = %{tl_version}, tex(gsmi2074.tfm) = %{tl_version}
Provides:       tex(gsmi2488.tfm) = %{tl_version}, tex(gsmi2986.tfm) = %{tl_version}
Provides:       tex(gsmi3583.tfm) = %{tl_version}, tex(gsmn0500.tfm) = %{tl_version}
Provides:       tex(gsmn0600.tfm) = %{tl_version}, tex(gsmn0700.tfm) = %{tl_version}
Provides:       tex(gsmn0800.tfm) = %{tl_version}, tex(gsmn0900.tfm) = %{tl_version}
Provides:       tex(gsmn1000.tfm) = %{tl_version}, tex(gsmn1095.tfm) = %{tl_version}
Provides:       tex(gsmn1200.tfm) = %{tl_version}, tex(gsmn1440.tfm) = %{tl_version}
Provides:       tex(gsmn1728.tfm) = %{tl_version}, tex(gsmn2074.tfm) = %{tl_version}
Provides:       tex(gsmn2488.tfm) = %{tl_version}, tex(gsmn2986.tfm) = %{tl_version}
Provides:       tex(gsmn3583.tfm) = %{tl_version}, tex(gsmo0500.tfm) = %{tl_version}
Provides:       tex(gsmo0600.tfm) = %{tl_version}, tex(gsmo0700.tfm) = %{tl_version}
Provides:       tex(gsmo0800.tfm) = %{tl_version}, tex(gsmo0900.tfm) = %{tl_version}
Provides:       tex(gsmo1000.tfm) = %{tl_version}, tex(gsmo1095.tfm) = %{tl_version}
Provides:       tex(gsmo1200.tfm) = %{tl_version}, tex(gsmo1440.tfm) = %{tl_version}
Provides:       tex(gsmo1728.tfm) = %{tl_version}, tex(gsmo2074.tfm) = %{tl_version}
Provides:       tex(gsmo2488.tfm) = %{tl_version}, tex(gsmo2986.tfm) = %{tl_version}
Provides:       tex(gsmo3583.tfm) = %{tl_version}, tex(gsmu0500.tfm) = %{tl_version}
Provides:       tex(gsmu0600.tfm) = %{tl_version}, tex(gsmu0700.tfm) = %{tl_version}
Provides:       tex(gsmu0800.tfm) = %{tl_version}, tex(gsmu0900.tfm) = %{tl_version}
Provides:       tex(gsmu1000.tfm) = %{tl_version}, tex(gsmu1095.tfm) = %{tl_version}
Provides:       tex(gsmu1200.tfm) = %{tl_version}, tex(gsmu1440.tfm) = %{tl_version}
Provides:       tex(gsmu1728.tfm) = %{tl_version}, tex(gsmu2074.tfm) = %{tl_version}
Provides:       tex(gsmu2488.tfm) = %{tl_version}, tex(gsmu2986.tfm) = %{tl_version}
Provides:       tex(gsmu3583.tfm) = %{tl_version}, tex(gsxa0500.tfm) = %{tl_version}
Provides:       tex(gsxa0600.tfm) = %{tl_version}, tex(gsxa0700.tfm) = %{tl_version}
Provides:       tex(gsxa0800.tfm) = %{tl_version}, tex(gsxa0900.tfm) = %{tl_version}
Provides:       tex(gsxa1000.tfm) = %{tl_version}, tex(gsxa1095.tfm) = %{tl_version}
Provides:       tex(gsxa1200.tfm) = %{tl_version}, tex(gsxa1440.tfm) = %{tl_version}
Provides:       tex(gsxa1728.tfm) = %{tl_version}, tex(gsxa2074.tfm) = %{tl_version}
Provides:       tex(gsxa2488.tfm) = %{tl_version}, tex(gsxa2986.tfm) = %{tl_version}
Provides:       tex(gsxa3583.tfm) = %{tl_version}, tex(gsxc0500.tfm) = %{tl_version}
Provides:       tex(gsxc0600.tfm) = %{tl_version}, tex(gsxc0700.tfm) = %{tl_version}
Provides:       tex(gsxc0800.tfm) = %{tl_version}, tex(gsxc0900.tfm) = %{tl_version}
Provides:       tex(gsxc1000.tfm) = %{tl_version}, tex(gsxc1095.tfm) = %{tl_version}
Provides:       tex(gsxc1200.tfm) = %{tl_version}, tex(gsxc1440.tfm) = %{tl_version}
Provides:       tex(gsxc1728.tfm) = %{tl_version}, tex(gsxc2074.tfm) = %{tl_version}
Provides:       tex(gsxc2488.tfm) = %{tl_version}, tex(gsxc2986.tfm) = %{tl_version}
Provides:       tex(gsxc3583.tfm) = %{tl_version}, tex(gsxe0500.tfm) = %{tl_version}
Provides:       tex(gsxe0600.tfm) = %{tl_version}, tex(gsxe0700.tfm) = %{tl_version}
Provides:       tex(gsxe0800.tfm) = %{tl_version}, tex(gsxe0900.tfm) = %{tl_version}
Provides:       tex(gsxe1000.tfm) = %{tl_version}, tex(gsxe1095.tfm) = %{tl_version}
Provides:       tex(gsxe1200.tfm) = %{tl_version}, tex(gsxe1440.tfm) = %{tl_version}
Provides:       tex(gsxe1728.tfm) = %{tl_version}, tex(gsxe2074.tfm) = %{tl_version}
Provides:       tex(gsxe2488.tfm) = %{tl_version}, tex(gsxe2986.tfm) = %{tl_version}
Provides:       tex(gsxe3583.tfm) = %{tl_version}, tex(gsxi0500.tfm) = %{tl_version}
Provides:       tex(gsxi0600.tfm) = %{tl_version}, tex(gsxi0700.tfm) = %{tl_version}
Provides:       tex(gsxi0800.tfm) = %{tl_version}, tex(gsxi0900.tfm) = %{tl_version}
Provides:       tex(gsxi1000.tfm) = %{tl_version}, tex(gsxi1095.tfm) = %{tl_version}
Provides:       tex(gsxi1200.tfm) = %{tl_version}, tex(gsxi1440.tfm) = %{tl_version}
Provides:       tex(gsxi1728.tfm) = %{tl_version}, tex(gsxi2074.tfm) = %{tl_version}
Provides:       tex(gsxi2488.tfm) = %{tl_version}, tex(gsxi2986.tfm) = %{tl_version}
Provides:       tex(gsxi3583.tfm) = %{tl_version}, tex(gsxn0500.tfm) = %{tl_version}
Provides:       tex(gsxn0600.tfm) = %{tl_version}, tex(gsxn0700.tfm) = %{tl_version}
Provides:       tex(gsxn0800.tfm) = %{tl_version}, tex(gsxn0900.tfm) = %{tl_version}
Provides:       tex(gsxn1000.tfm) = %{tl_version}, tex(gsxn1095.tfm) = %{tl_version}
Provides:       tex(gsxn1200.tfm) = %{tl_version}, tex(gsxn1440.tfm) = %{tl_version}
Provides:       tex(gsxn1728.tfm) = %{tl_version}, tex(gsxn2074.tfm) = %{tl_version}
Provides:       tex(gsxn2488.tfm) = %{tl_version}, tex(gsxn2986.tfm) = %{tl_version}
Provides:       tex(gsxn3583.tfm) = %{tl_version}, tex(gsxo0500.tfm) = %{tl_version}
Provides:       tex(gsxo0600.tfm) = %{tl_version}, tex(gsxo0700.tfm) = %{tl_version}
Provides:       tex(gsxo0800.tfm) = %{tl_version}, tex(gsxo0900.tfm) = %{tl_version}
Provides:       tex(gsxo1000.tfm) = %{tl_version}, tex(gsxo1095.tfm) = %{tl_version}
Provides:       tex(gsxo1200.tfm) = %{tl_version}, tex(gsxo1440.tfm) = %{tl_version}
Provides:       tex(gsxo1728.tfm) = %{tl_version}, tex(gsxo2074.tfm) = %{tl_version}
Provides:       tex(gsxo2488.tfm) = %{tl_version}, tex(gsxo2986.tfm) = %{tl_version}
Provides:       tex(gsxo3583.tfm) = %{tl_version}, tex(gsxu0500.tfm) = %{tl_version}
Provides:       tex(gsxu0600.tfm) = %{tl_version}, tex(gsxu0700.tfm) = %{tl_version}
Provides:       tex(gsxu0800.tfm) = %{tl_version}, tex(gsxu0900.tfm) = %{tl_version}
Provides:       tex(gsxu1000.tfm) = %{tl_version}, tex(gsxu1095.tfm) = %{tl_version}
Provides:       tex(gsxu1200.tfm) = %{tl_version}, tex(gsxu1440.tfm) = %{tl_version}
Provides:       tex(gsxu1728.tfm) = %{tl_version}, tex(gsxu2074.tfm) = %{tl_version}
Provides:       tex(gsxu2488.tfm) = %{tl_version}, tex(gsxu2986.tfm) = %{tl_version}
Provides:       tex(gsxu3583.tfm) = %{tl_version}, tex(gttc0500.tfm) = %{tl_version}
Provides:       tex(gttc0600.tfm) = %{tl_version}, tex(gttc0700.tfm) = %{tl_version}
Provides:       tex(gttc0800.tfm) = %{tl_version}, tex(gttc0900.tfm) = %{tl_version}
Provides:       tex(gttc1000.tfm) = %{tl_version}, tex(gttc1095.tfm) = %{tl_version}
Provides:       tex(gttc1200.tfm) = %{tl_version}, tex(gttc1440.tfm) = %{tl_version}
Provides:       tex(gttc1728.tfm) = %{tl_version}, tex(gttc2074.tfm) = %{tl_version}
Provides:       tex(gttc2488.tfm) = %{tl_version}, tex(gttc2986.tfm) = %{tl_version}
Provides:       tex(gttc3583.tfm) = %{tl_version}, tex(gtti0500.tfm) = %{tl_version}
Provides:       tex(gtti0600.tfm) = %{tl_version}, tex(gtti0700.tfm) = %{tl_version}
Provides:       tex(gtti0800.tfm) = %{tl_version}, tex(gtti0900.tfm) = %{tl_version}
Provides:       tex(gtti1000.tfm) = %{tl_version}, tex(gtti1095.tfm) = %{tl_version}
Provides:       tex(gtti1200.tfm) = %{tl_version}, tex(gtti1440.tfm) = %{tl_version}
Provides:       tex(gtti1728.tfm) = %{tl_version}, tex(gtti2074.tfm) = %{tl_version}
Provides:       tex(gtti2488.tfm) = %{tl_version}, tex(gtti2986.tfm) = %{tl_version}
Provides:       tex(gtti3583.tfm) = %{tl_version}, tex(gttn0500.tfm) = %{tl_version}
Provides:       tex(gttn0600.tfm) = %{tl_version}, tex(gttn0700.tfm) = %{tl_version}
Provides:       tex(gttn0800.tfm) = %{tl_version}, tex(gttn0900.tfm) = %{tl_version}
Provides:       tex(gttn1000.tfm) = %{tl_version}, tex(gttn1095.tfm) = %{tl_version}
Provides:       tex(gttn1200.tfm) = %{tl_version}, tex(gttn1440.tfm) = %{tl_version}
Provides:       tex(gttn1728.tfm) = %{tl_version}, tex(gttn2074.tfm) = %{tl_version}
Provides:       tex(gttn2488.tfm) = %{tl_version}, tex(gttn2986.tfm) = %{tl_version}
Provides:       tex(gttn3583.tfm) = %{tl_version}, tex(gtto0500.tfm) = %{tl_version}
Provides:       tex(gtto0600.tfm) = %{tl_version}, tex(gtto0700.tfm) = %{tl_version}
Provides:       tex(gtto0800.tfm) = %{tl_version}, tex(gtto0900.tfm) = %{tl_version}
Provides:       tex(gtto1000.tfm) = %{tl_version}, tex(gtto1095.tfm) = %{tl_version}
Provides:       tex(gtto1200.tfm) = %{tl_version}, tex(gtto1440.tfm) = %{tl_version}
Provides:       tex(gtto1728.tfm) = %{tl_version}, tex(gtto2074.tfm) = %{tl_version}
Provides:       tex(gtto2488.tfm) = %{tl_version}, tex(gtto2986.tfm) = %{tl_version}
Provides:       tex(gtto3583.tfm) = %{tl_version}, tex(gttu0500.tfm) = %{tl_version}
Provides:       tex(gttu0600.tfm) = %{tl_version}, tex(gttu0700.tfm) = %{tl_version}
Provides:       tex(gttu0800.tfm) = %{tl_version}, tex(gttu0900.tfm) = %{tl_version}
Provides:       tex(gttu1000.tfm) = %{tl_version}, tex(gttu1095.tfm) = %{tl_version}
Provides:       tex(gttu1200.tfm) = %{tl_version}, tex(gttu1440.tfm) = %{tl_version}
Provides:       tex(gttu1728.tfm) = %{tl_version}, tex(gttu2074.tfm) = %{tl_version}
Provides:       tex(gttu2488.tfm) = %{tl_version}, tex(gttu2986.tfm) = %{tl_version}
Provides:       tex(gttu3583.tfm) = %{tl_version}, tex(glic0700.pfb) = %{tl_version}
Provides:       tex(glic0800.pfb) = %{tl_version}, tex(glic1000.pfb) = %{tl_version}
Provides:       tex(glic1200.pfb) = %{tl_version}, tex(glic1382.pfb) = %{tl_version}
Provides:       tex(glic1659.pfb) = %{tl_version}, tex(glic1991.pfb) = %{tl_version}
Provides:       tex(glic2389.pfb) = %{tl_version}, tex(glic2866.pfb) = %{tl_version}
Provides:       tex(glic3440.pfb) = %{tl_version}, tex(glic4128.pfb) = %{tl_version}
Provides:       tex(glii0700.pfb) = %{tl_version}, tex(glii0800.pfb) = %{tl_version}
Provides:       tex(glii1000.pfb) = %{tl_version}, tex(glii1200.pfb) = %{tl_version}
Provides:       tex(glii1382.pfb) = %{tl_version}, tex(glii1659.pfb) = %{tl_version}
Provides:       tex(glii1991.pfb) = %{tl_version}, tex(glii2389.pfb) = %{tl_version}
Provides:       tex(glii2866.pfb) = %{tl_version}, tex(glii3440.pfb) = %{tl_version}
Provides:       tex(glii4128.pfb) = %{tl_version}, tex(glin0700.pfb) = %{tl_version}
Provides:       tex(glin0800.pfb) = %{tl_version}, tex(glin1000.pfb) = %{tl_version}
Provides:       tex(glin1200.pfb) = %{tl_version}, tex(glin1382.pfb) = %{tl_version}
Provides:       tex(glin1659.pfb) = %{tl_version}, tex(glin1991.pfb) = %{tl_version}
Provides:       tex(glin2389.pfb) = %{tl_version}, tex(glin2866.pfb) = %{tl_version}
Provides:       tex(glin3440.pfb) = %{tl_version}, tex(glin4128.pfb) = %{tl_version}
Provides:       tex(glio0700.pfb) = %{tl_version}, tex(glio0800.pfb) = %{tl_version}
Provides:       tex(glio1000.pfb) = %{tl_version}, tex(glio1200.pfb) = %{tl_version}
Provides:       tex(glio1382.pfb) = %{tl_version}, tex(glio1659.pfb) = %{tl_version}
Provides:       tex(glio1991.pfb) = %{tl_version}, tex(glio2389.pfb) = %{tl_version}
Provides:       tex(glio2866.pfb) = %{tl_version}, tex(glio3440.pfb) = %{tl_version}
Provides:       tex(glio4128.pfb) = %{tl_version}, tex(gliu0700.pfb) = %{tl_version}
Provides:       tex(gliu0800.pfb) = %{tl_version}, tex(gliu1000.pfb) = %{tl_version}
Provides:       tex(gliu1200.pfb) = %{tl_version}, tex(gliu1382.pfb) = %{tl_version}
Provides:       tex(gliu1659.pfb) = %{tl_version}, tex(gliu1991.pfb) = %{tl_version}
Provides:       tex(gliu2389.pfb) = %{tl_version}, tex(gliu2866.pfb) = %{tl_version}
Provides:       tex(gliu3440.pfb) = %{tl_version}, tex(gliu4128.pfb) = %{tl_version}
Provides:       tex(gljc0700.pfb) = %{tl_version}, tex(gljc0800.pfb) = %{tl_version}
Provides:       tex(gljc1000.pfb) = %{tl_version}, tex(gljc1200.pfb) = %{tl_version}
Provides:       tex(gljc1382.pfb) = %{tl_version}, tex(gljc1659.pfb) = %{tl_version}
Provides:       tex(gljc1991.pfb) = %{tl_version}, tex(gljc2389.pfb) = %{tl_version}
Provides:       tex(gljc2866.pfb) = %{tl_version}, tex(gljc3440.pfb) = %{tl_version}
Provides:       tex(gljc4128.pfb) = %{tl_version}, tex(gljn0700.pfb) = %{tl_version}
Provides:       tex(gljn0800.pfb) = %{tl_version}, tex(gljn1000.pfb) = %{tl_version}
Provides:       tex(gljn1200.pfb) = %{tl_version}, tex(gljn1382.pfb) = %{tl_version}
Provides:       tex(gljn1659.pfb) = %{tl_version}, tex(gljn1991.pfb) = %{tl_version}
Provides:       tex(gljn2389.pfb) = %{tl_version}, tex(gljn2866.pfb) = %{tl_version}
Provides:       tex(gljn3440.pfb) = %{tl_version}, tex(gljn4128.pfb) = %{tl_version}
Provides:       tex(gljo0700.pfb) = %{tl_version}, tex(gljo0800.pfb) = %{tl_version}
Provides:       tex(gljo1000.pfb) = %{tl_version}, tex(gljo1200.pfb) = %{tl_version}
Provides:       tex(gljo1382.pfb) = %{tl_version}, tex(gljo1659.pfb) = %{tl_version}
Provides:       tex(gljo1991.pfb) = %{tl_version}, tex(gljo2389.pfb) = %{tl_version}
Provides:       tex(gljo2866.pfb) = %{tl_version}, tex(gljo3440.pfb) = %{tl_version}
Provides:       tex(gljo4128.pfb) = %{tl_version}, tex(glmc0700.pfb) = %{tl_version}
Provides:       tex(glmc0800.pfb) = %{tl_version}, tex(glmc1000.pfb) = %{tl_version}
Provides:       tex(glmc1200.pfb) = %{tl_version}, tex(glmc1382.pfb) = %{tl_version}
Provides:       tex(glmc1659.pfb) = %{tl_version}, tex(glmc1991.pfb) = %{tl_version}
Provides:       tex(glmc2389.pfb) = %{tl_version}, tex(glmc2866.pfb) = %{tl_version}
Provides:       tex(glmc3440.pfb) = %{tl_version}, tex(glmc4128.pfb) = %{tl_version}
Provides:       tex(glmi0700.pfb) = %{tl_version}, tex(glmi0800.pfb) = %{tl_version}
Provides:       tex(glmi1000.pfb) = %{tl_version}, tex(glmi1200.pfb) = %{tl_version}
Provides:       tex(glmi1382.pfb) = %{tl_version}, tex(glmi1659.pfb) = %{tl_version}
Provides:       tex(glmi1991.pfb) = %{tl_version}, tex(glmi2389.pfb) = %{tl_version}
Provides:       tex(glmi2866.pfb) = %{tl_version}, tex(glmi3440.pfb) = %{tl_version}
Provides:       tex(glmi4128.pfb) = %{tl_version}, tex(glmn0700.pfb) = %{tl_version}
Provides:       tex(glmn0800.pfb) = %{tl_version}, tex(glmn1000.pfb) = %{tl_version}
Provides:       tex(glmn1200.pfb) = %{tl_version}, tex(glmn1382.pfb) = %{tl_version}
Provides:       tex(glmn1659.pfb) = %{tl_version}, tex(glmn1991.pfb) = %{tl_version}
Provides:       tex(glmn2389.pfb) = %{tl_version}, tex(glmn2866.pfb) = %{tl_version}
Provides:       tex(glmn3440.pfb) = %{tl_version}, tex(glmn4128.pfb) = %{tl_version}
Provides:       tex(glmo0700.pfb) = %{tl_version}, tex(glmo0800.pfb) = %{tl_version}
Provides:       tex(glmo1000.pfb) = %{tl_version}, tex(glmo1200.pfb) = %{tl_version}
Provides:       tex(glmo1382.pfb) = %{tl_version}, tex(glmo1659.pfb) = %{tl_version}
Provides:       tex(glmo1991.pfb) = %{tl_version}, tex(glmo2389.pfb) = %{tl_version}
Provides:       tex(glmo2866.pfb) = %{tl_version}, tex(glmo3440.pfb) = %{tl_version}
Provides:       tex(glmo4128.pfb) = %{tl_version}, tex(glmu0700.pfb) = %{tl_version}
Provides:       tex(glmu0800.pfb) = %{tl_version}, tex(glmu1000.pfb) = %{tl_version}
Provides:       tex(glmu1200.pfb) = %{tl_version}, tex(glmu1382.pfb) = %{tl_version}
Provides:       tex(glmu1659.pfb) = %{tl_version}, tex(glmu1991.pfb) = %{tl_version}
Provides:       tex(glmu2389.pfb) = %{tl_version}, tex(glmu2866.pfb) = %{tl_version}
Provides:       tex(glmu3440.pfb) = %{tl_version}, tex(glmu4128.pfb) = %{tl_version}
Provides:       tex(gltc0700.pfb) = %{tl_version}, tex(gltc0800.pfb) = %{tl_version}
Provides:       tex(gltc1000.pfb) = %{tl_version}, tex(gltc1200.pfb) = %{tl_version}
Provides:       tex(gltc1382.pfb) = %{tl_version}, tex(gltc1659.pfb) = %{tl_version}
Provides:       tex(gltc1991.pfb) = %{tl_version}, tex(gltc2389.pfb) = %{tl_version}
Provides:       tex(gltc2866.pfb) = %{tl_version}, tex(gltc3440.pfb) = %{tl_version}
Provides:       tex(gltc4128.pfb) = %{tl_version}, tex(gltn0700.pfb) = %{tl_version}
Provides:       tex(gltn0800.pfb) = %{tl_version}, tex(gltn1000.pfb) = %{tl_version}
Provides:       tex(gltn1200.pfb) = %{tl_version}, tex(gltn1382.pfb) = %{tl_version}
Provides:       tex(gltn1659.pfb) = %{tl_version}, tex(gltn1991.pfb) = %{tl_version}
Provides:       tex(gltn2389.pfb) = %{tl_version}, tex(gltn2866.pfb) = %{tl_version}
Provides:       tex(gltn3440.pfb) = %{tl_version}, tex(gltn4128.pfb) = %{tl_version}
Provides:       tex(glto0700.pfb) = %{tl_version}, tex(glto0800.pfb) = %{tl_version}
Provides:       tex(glto1000.pfb) = %{tl_version}, tex(glto1200.pfb) = %{tl_version}
Provides:       tex(glto1382.pfb) = %{tl_version}, tex(glto1659.pfb) = %{tl_version}
Provides:       tex(glto1991.pfb) = %{tl_version}, tex(glto2389.pfb) = %{tl_version}
Provides:       tex(glto2866.pfb) = %{tl_version}, tex(glto3440.pfb) = %{tl_version}
Provides:       tex(glto4128.pfb) = %{tl_version}, tex(glwc0700.pfb) = %{tl_version}
Provides:       tex(glwc0800.pfb) = %{tl_version}, tex(glwc1000.pfb) = %{tl_version}
Provides:       tex(glwc1200.pfb) = %{tl_version}, tex(glwc1382.pfb) = %{tl_version}
Provides:       tex(glwc1659.pfb) = %{tl_version}, tex(glwc1991.pfb) = %{tl_version}
Provides:       tex(glwc2389.pfb) = %{tl_version}, tex(glwc2866.pfb) = %{tl_version}
Provides:       tex(glwc3440.pfb) = %{tl_version}, tex(glwc4128.pfb) = %{tl_version}
Provides:       tex(glwi0700.pfb) = %{tl_version}, tex(glwi0800.pfb) = %{tl_version}
Provides:       tex(glwi1000.pfb) = %{tl_version}, tex(glwi1200.pfb) = %{tl_version}
Provides:       tex(glwi1382.pfb) = %{tl_version}, tex(glwi1659.pfb) = %{tl_version}
Provides:       tex(glwi1991.pfb) = %{tl_version}, tex(glwi2389.pfb) = %{tl_version}
Provides:       tex(glwi2866.pfb) = %{tl_version}, tex(glwi3440.pfb) = %{tl_version}
Provides:       tex(glwi4128.pfb) = %{tl_version}, tex(glwn0700.pfb) = %{tl_version}
Provides:       tex(glwn0800.pfb) = %{tl_version}, tex(glwn1000.pfb) = %{tl_version}
Provides:       tex(glwn1200.pfb) = %{tl_version}, tex(glwn1382.pfb) = %{tl_version}
Provides:       tex(glwn1659.pfb) = %{tl_version}, tex(glwn1991.pfb) = %{tl_version}
Provides:       tex(glwn2389.pfb) = %{tl_version}, tex(glwn2866.pfb) = %{tl_version}
Provides:       tex(glwn3440.pfb) = %{tl_version}, tex(glwn4128.pfb) = %{tl_version}
Provides:       tex(glwo0700.pfb) = %{tl_version}, tex(glwo0800.pfb) = %{tl_version}
Provides:       tex(glwo1000.pfb) = %{tl_version}, tex(glwo1200.pfb) = %{tl_version}
Provides:       tex(glwo1382.pfb) = %{tl_version}, tex(glwo1659.pfb) = %{tl_version}
Provides:       tex(glwo1991.pfb) = %{tl_version}, tex(glwo2389.pfb) = %{tl_version}
Provides:       tex(glwo2866.pfb) = %{tl_version}, tex(glwo3440.pfb) = %{tl_version}
Provides:       tex(glwo4128.pfb) = %{tl_version}, tex(glwu0700.pfb) = %{tl_version}
Provides:       tex(glwu0800.pfb) = %{tl_version}, tex(glwu1000.pfb) = %{tl_version}
Provides:       tex(glwu1200.pfb) = %{tl_version}, tex(glwu1382.pfb) = %{tl_version}
Provides:       tex(glwu1659.pfb) = %{tl_version}, tex(glwu1991.pfb) = %{tl_version}
Provides:       tex(glwu2389.pfb) = %{tl_version}, tex(glwu2866.pfb) = %{tl_version}
Provides:       tex(glwu3440.pfb) = %{tl_version}, tex(glwu4128.pfb) = %{tl_version}
Provides:       tex(glxc0700.pfb) = %{tl_version}, tex(glxc0800.pfb) = %{tl_version}
Provides:       tex(glxc1000.pfb) = %{tl_version}, tex(glxc1200.pfb) = %{tl_version}
Provides:       tex(glxc1382.pfb) = %{tl_version}, tex(glxc1659.pfb) = %{tl_version}
Provides:       tex(glxc1991.pfb) = %{tl_version}, tex(glxc2389.pfb) = %{tl_version}
Provides:       tex(glxc2866.pfb) = %{tl_version}, tex(glxc3440.pfb) = %{tl_version}
Provides:       tex(glxc4128.pfb) = %{tl_version}, tex(glxi0700.pfb) = %{tl_version}
Provides:       tex(glxi0800.pfb) = %{tl_version}, tex(glxi1000.pfb) = %{tl_version}
Provides:       tex(glxi1200.pfb) = %{tl_version}, tex(glxi1382.pfb) = %{tl_version}
Provides:       tex(glxi1659.pfb) = %{tl_version}, tex(glxi1991.pfb) = %{tl_version}
Provides:       tex(glxi2389.pfb) = %{tl_version}, tex(glxi2866.pfb) = %{tl_version}
Provides:       tex(glxi3440.pfb) = %{tl_version}, tex(glxi4128.pfb) = %{tl_version}
Provides:       tex(glxn0700.pfb) = %{tl_version}, tex(glxn0800.pfb) = %{tl_version}
Provides:       tex(glxn1000.pfb) = %{tl_version}, tex(glxn1200.pfb) = %{tl_version}
Provides:       tex(glxn1382.pfb) = %{tl_version}, tex(glxn1659.pfb) = %{tl_version}
Provides:       tex(glxn1991.pfb) = %{tl_version}, tex(glxn2389.pfb) = %{tl_version}
Provides:       tex(glxn2866.pfb) = %{tl_version}, tex(glxn3440.pfb) = %{tl_version}
Provides:       tex(glxn4128.pfb) = %{tl_version}, tex(glxo0700.pfb) = %{tl_version}
Provides:       tex(glxo0800.pfb) = %{tl_version}, tex(glxo1000.pfb) = %{tl_version}
Provides:       tex(glxo1200.pfb) = %{tl_version}, tex(glxo1382.pfb) = %{tl_version}
Provides:       tex(glxo1659.pfb) = %{tl_version}, tex(glxo1991.pfb) = %{tl_version}
Provides:       tex(glxo2389.pfb) = %{tl_version}, tex(glxo2866.pfb) = %{tl_version}
Provides:       tex(glxo3440.pfb) = %{tl_version}, tex(glxo4128.pfb) = %{tl_version}
Provides:       tex(glxu0700.pfb) = %{tl_version}, tex(glxu0800.pfb) = %{tl_version}
Provides:       tex(glxu1000.pfb) = %{tl_version}, tex(glxu1200.pfb) = %{tl_version}
Provides:       tex(glxu1382.pfb) = %{tl_version}, tex(glxu1659.pfb) = %{tl_version}
Provides:       tex(glxu1991.pfb) = %{tl_version}, tex(glxu2389.pfb) = %{tl_version}
Provides:       tex(glxu2866.pfb) = %{tl_version}, tex(glxu3440.pfb) = %{tl_version}
Provides:       tex(glxu4128.pfb) = %{tl_version}, tex(gmmn0500.pfb) = %{tl_version}
Provides:       tex(gmmn0600.pfb) = %{tl_version}, tex(gmmn0700.pfb) = %{tl_version}
Provides:       tex(gmmn0800.pfb) = %{tl_version}, tex(gmmn0900.pfb) = %{tl_version}
Provides:       tex(gmmn1000.pfb) = %{tl_version}, tex(gmmn1095.pfb) = %{tl_version}
Provides:       tex(gmmn1200.pfb) = %{tl_version}, tex(gmmn1440.pfb) = %{tl_version}
Provides:       tex(gmmn1728.pfb) = %{tl_version}, tex(gmmn2074.pfb) = %{tl_version}
Provides:       tex(gmmn2488.pfb) = %{tl_version}, tex(gmmn2986.pfb) = %{tl_version}
Provides:       tex(gmmn3583.pfb) = %{tl_version}, tex(gmmo0500.pfb) = %{tl_version}
Provides:       tex(gmmo0600.pfb) = %{tl_version}, tex(gmmo0700.pfb) = %{tl_version}
Provides:       tex(gmmo0800.pfb) = %{tl_version}, tex(gmmo0900.pfb) = %{tl_version}
Provides:       tex(gmmo1000.pfb) = %{tl_version}, tex(gmmo1095.pfb) = %{tl_version}
Provides:       tex(gmmo1200.pfb) = %{tl_version}, tex(gmmo1440.pfb) = %{tl_version}
Provides:       tex(gmmo1728.pfb) = %{tl_version}, tex(gmmo2074.pfb) = %{tl_version}
Provides:       tex(gmmo2488.pfb) = %{tl_version}, tex(gmmo2986.pfb) = %{tl_version}
Provides:       tex(gmmo3583.pfb) = %{tl_version}, tex(gmtr0500.pfb) = %{tl_version}
Provides:       tex(gmtr0600.pfb) = %{tl_version}, tex(gmtr0700.pfb) = %{tl_version}
Provides:       tex(gmtr0800.pfb) = %{tl_version}, tex(gmtr0900.pfb) = %{tl_version}
Provides:       tex(gmtr1000.pfb) = %{tl_version}, tex(gmtr1095.pfb) = %{tl_version}
Provides:       tex(gmtr1200.pfb) = %{tl_version}, tex(gmtr1440.pfb) = %{tl_version}
Provides:       tex(gmtr1728.pfb) = %{tl_version}, tex(gmtr2074.pfb) = %{tl_version}
Provides:       tex(gmtr2488.pfb) = %{tl_version}, tex(gmtr2986.pfb) = %{tl_version}
Provides:       tex(gmtr3583.pfb) = %{tl_version}, tex(gmxn0500.pfb) = %{tl_version}
Provides:       tex(gmxn0600.pfb) = %{tl_version}, tex(gmxn0700.pfb) = %{tl_version}
Provides:       tex(gmxn0800.pfb) = %{tl_version}, tex(gmxn0900.pfb) = %{tl_version}
Provides:       tex(gmxn1000.pfb) = %{tl_version}, tex(gmxn1095.pfb) = %{tl_version}
Provides:       tex(gmxn1200.pfb) = %{tl_version}, tex(gmxn1440.pfb) = %{tl_version}
Provides:       tex(gmxn1728.pfb) = %{tl_version}, tex(gmxn2074.pfb) = %{tl_version}
Provides:       tex(gmxn2488.pfb) = %{tl_version}, tex(gmxn2986.pfb) = %{tl_version}
Provides:       tex(gmxn3583.pfb) = %{tl_version}, tex(gmxo0500.pfb) = %{tl_version}
Provides:       tex(gmxo0600.pfb) = %{tl_version}, tex(gmxo0700.pfb) = %{tl_version}
Provides:       tex(gmxo0800.pfb) = %{tl_version}, tex(gmxo0900.pfb) = %{tl_version}
Provides:       tex(gmxo1000.pfb) = %{tl_version}, tex(gmxo1095.pfb) = %{tl_version}
Provides:       tex(gmxo1200.pfb) = %{tl_version}, tex(gmxo1440.pfb) = %{tl_version}
Provides:       tex(gmxo1728.pfb) = %{tl_version}, tex(gmxo2074.pfb) = %{tl_version}
Provides:       tex(gmxo2488.pfb) = %{tl_version}, tex(gmxo2986.pfb) = %{tl_version}
Provides:       tex(gmxo3583.pfb) = %{tl_version}, tex(gomc0500.pfb) = %{tl_version}
Provides:       tex(gomc0600.pfb) = %{tl_version}, tex(gomc0700.pfb) = %{tl_version}
Provides:       tex(gomc0800.pfb) = %{tl_version}, tex(gomc0900.pfb) = %{tl_version}
Provides:       tex(gomc1000.pfb) = %{tl_version}, tex(gomc1095.pfb) = %{tl_version}
Provides:       tex(gomc1200.pfb) = %{tl_version}, tex(gomc1440.pfb) = %{tl_version}
Provides:       tex(gomc1728.pfb) = %{tl_version}, tex(gomc2074.pfb) = %{tl_version}
Provides:       tex(gomc2488.pfb) = %{tl_version}, tex(gomc2986.pfb) = %{tl_version}
Provides:       tex(gomc3583.pfb) = %{tl_version}, tex(gomi0500.pfb) = %{tl_version}
Provides:       tex(gomi0600.pfb) = %{tl_version}, tex(gomi0700.pfb) = %{tl_version}
Provides:       tex(gomi0800.pfb) = %{tl_version}, tex(gomi0900.pfb) = %{tl_version}
Provides:       tex(gomi1000.pfb) = %{tl_version}, tex(gomi1095.pfb) = %{tl_version}
Provides:       tex(gomi1200.pfb) = %{tl_version}, tex(gomi1440.pfb) = %{tl_version}
Provides:       tex(gomi1728.pfb) = %{tl_version}, tex(gomi2074.pfb) = %{tl_version}
Provides:       tex(gomi2488.pfb) = %{tl_version}, tex(gomi2986.pfb) = %{tl_version}
Provides:       tex(gomi3583.pfb) = %{tl_version}, tex(gomn0500.pfb) = %{tl_version}
Provides:       tex(gomn0600.pfb) = %{tl_version}, tex(gomn0700.pfb) = %{tl_version}
Provides:       tex(gomn0800.pfb) = %{tl_version}, tex(gomn0900.pfb) = %{tl_version}
Provides:       tex(gomn1000.pfb) = %{tl_version}, tex(gomn1095.pfb) = %{tl_version}
Provides:       tex(gomn1200.pfb) = %{tl_version}, tex(gomn1440.pfb) = %{tl_version}
Provides:       tex(gomn1728.pfb) = %{tl_version}, tex(gomn2074.pfb) = %{tl_version}
Provides:       tex(gomn2488.pfb) = %{tl_version}, tex(gomn2986.pfb) = %{tl_version}
Provides:       tex(gomn3583.pfb) = %{tl_version}, tex(gomo0500.pfb) = %{tl_version}
Provides:       tex(gomo0600.pfb) = %{tl_version}, tex(gomo0700.pfb) = %{tl_version}
Provides:       tex(gomo0800.pfb) = %{tl_version}, tex(gomo0900.pfb) = %{tl_version}
Provides:       tex(gomo1000.pfb) = %{tl_version}, tex(gomo1095.pfb) = %{tl_version}
Provides:       tex(gomo1200.pfb) = %{tl_version}, tex(gomo1440.pfb) = %{tl_version}
Provides:       tex(gomo1728.pfb) = %{tl_version}, tex(gomo2074.pfb) = %{tl_version}
Provides:       tex(gomo2488.pfb) = %{tl_version}, tex(gomo2986.pfb) = %{tl_version}
Provides:       tex(gomo3583.pfb) = %{tl_version}, tex(gomu0500.pfb) = %{tl_version}
Provides:       tex(gomu0600.pfb) = %{tl_version}, tex(gomu0700.pfb) = %{tl_version}
Provides:       tex(gomu0800.pfb) = %{tl_version}, tex(gomu0900.pfb) = %{tl_version}
Provides:       tex(gomu1000.pfb) = %{tl_version}, tex(gomu1095.pfb) = %{tl_version}
Provides:       tex(gomu1200.pfb) = %{tl_version}, tex(gomu1440.pfb) = %{tl_version}
Provides:       tex(gomu1728.pfb) = %{tl_version}, tex(gomu2074.pfb) = %{tl_version}
Provides:       tex(gomu2488.pfb) = %{tl_version}, tex(gomu2986.pfb) = %{tl_version}
Provides:       tex(gomu3583.pfb) = %{tl_version}, tex(goxc0500.pfb) = %{tl_version}
Provides:       tex(goxc0600.pfb) = %{tl_version}, tex(goxc0700.pfb) = %{tl_version}
Provides:       tex(goxc0800.pfb) = %{tl_version}, tex(goxc0900.pfb) = %{tl_version}
Provides:       tex(goxc1000.pfb) = %{tl_version}, tex(goxc1095.pfb) = %{tl_version}
Provides:       tex(goxc1200.pfb) = %{tl_version}, tex(goxc1440.pfb) = %{tl_version}
Provides:       tex(goxc1728.pfb) = %{tl_version}, tex(goxc2074.pfb) = %{tl_version}
Provides:       tex(goxc2488.pfb) = %{tl_version}, tex(goxc2986.pfb) = %{tl_version}
Provides:       tex(goxc3583.pfb) = %{tl_version}, tex(goxi0500.pfb) = %{tl_version}
Provides:       tex(goxi0600.pfb) = %{tl_version}, tex(goxi0700.pfb) = %{tl_version}
Provides:       tex(goxi0800.pfb) = %{tl_version}, tex(goxi0900.pfb) = %{tl_version}
Provides:       tex(goxi1000.pfb) = %{tl_version}, tex(goxi1095.pfb) = %{tl_version}
Provides:       tex(goxi1200.pfb) = %{tl_version}, tex(goxi1440.pfb) = %{tl_version}
Provides:       tex(goxi1728.pfb) = %{tl_version}, tex(goxi2074.pfb) = %{tl_version}
Provides:       tex(goxi2488.pfb) = %{tl_version}, tex(goxi2986.pfb) = %{tl_version}
Provides:       tex(goxi3583.pfb) = %{tl_version}, tex(goxn0500.pfb) = %{tl_version}
Provides:       tex(goxn0600.pfb) = %{tl_version}, tex(goxn0700.pfb) = %{tl_version}
Provides:       tex(goxn0800.pfb) = %{tl_version}, tex(goxn0900.pfb) = %{tl_version}
Provides:       tex(goxn1000.pfb) = %{tl_version}, tex(goxn1095.pfb) = %{tl_version}
Provides:       tex(goxn1200.pfb) = %{tl_version}, tex(goxn1440.pfb) = %{tl_version}
Provides:       tex(goxn1728.pfb) = %{tl_version}, tex(goxn2074.pfb) = %{tl_version}
Provides:       tex(goxn2488.pfb) = %{tl_version}, tex(goxn2986.pfb) = %{tl_version}
Provides:       tex(goxn3583.pfb) = %{tl_version}, tex(goxo0500.pfb) = %{tl_version}
Provides:       tex(goxo0600.pfb) = %{tl_version}, tex(goxo0700.pfb) = %{tl_version}
Provides:       tex(goxo0800.pfb) = %{tl_version}, tex(goxo0900.pfb) = %{tl_version}
Provides:       tex(goxo1000.pfb) = %{tl_version}, tex(goxo1095.pfb) = %{tl_version}
Provides:       tex(goxo1200.pfb) = %{tl_version}, tex(goxo1440.pfb) = %{tl_version}
Provides:       tex(goxo1728.pfb) = %{tl_version}, tex(goxo2074.pfb) = %{tl_version}
Provides:       tex(goxo2488.pfb) = %{tl_version}, tex(goxo2986.pfb) = %{tl_version}
Provides:       tex(goxo3583.pfb) = %{tl_version}, tex(goxu0500.pfb) = %{tl_version}
Provides:       tex(goxu0600.pfb) = %{tl_version}, tex(goxu0700.pfb) = %{tl_version}
Provides:       tex(goxu0800.pfb) = %{tl_version}, tex(goxu0900.pfb) = %{tl_version}
Provides:       tex(goxu1000.pfb) = %{tl_version}, tex(goxu1095.pfb) = %{tl_version}
Provides:       tex(goxu1200.pfb) = %{tl_version}, tex(goxu1440.pfb) = %{tl_version}
Provides:       tex(goxu1728.pfb) = %{tl_version}, tex(goxu2074.pfb) = %{tl_version}
Provides:       tex(goxu2488.pfb) = %{tl_version}, tex(goxu2986.pfb) = %{tl_version}
Provides:       tex(goxu3583.pfb) = %{tl_version}, tex(grbl0500.pfb) = %{tl_version}
Provides:       tex(grbl0600.pfb) = %{tl_version}, tex(grbl0700.pfb) = %{tl_version}
Provides:       tex(grbl0800.pfb) = %{tl_version}, tex(grbl0900.pfb) = %{tl_version}
Provides:       tex(grbl1000.pfb) = %{tl_version}, tex(grbl1095.pfb) = %{tl_version}
Provides:       tex(grbl1200.pfb) = %{tl_version}, tex(grbl1440.pfb) = %{tl_version}
Provides:       tex(grbl1728.pfb) = %{tl_version}, tex(grbl2074.pfb) = %{tl_version}
Provides:       tex(grbl2488.pfb) = %{tl_version}, tex(grbl2986.pfb) = %{tl_version}
Provides:       tex(grbl3583.pfb) = %{tl_version}, tex(grmc0500.pfb) = %{tl_version}
Provides:       tex(grmc0600.pfb) = %{tl_version}, tex(grmc0700.pfb) = %{tl_version}
Provides:       tex(grmc0800.pfb) = %{tl_version}, tex(grmc0900.pfb) = %{tl_version}
Provides:       tex(grmc1000.pfb) = %{tl_version}, tex(grmc1095.pfb) = %{tl_version}
Provides:       tex(grmc1200.pfb) = %{tl_version}, tex(grmc1440.pfb) = %{tl_version}
Provides:       tex(grmc1728.pfb) = %{tl_version}, tex(grmc2074.pfb) = %{tl_version}
Provides:       tex(grmc2488.pfb) = %{tl_version}, tex(grmc2986.pfb) = %{tl_version}
Provides:       tex(grmc3583.pfb) = %{tl_version}, tex(grmi0500.pfb) = %{tl_version}
Provides:       tex(grmi0600.pfb) = %{tl_version}, tex(grmi0700.pfb) = %{tl_version}
Provides:       tex(grmi0800.pfb) = %{tl_version}, tex(grmi0900.pfb) = %{tl_version}
Provides:       tex(grmi1000.pfb) = %{tl_version}, tex(grmi1095.pfb) = %{tl_version}
Provides:       tex(grmi1200.pfb) = %{tl_version}, tex(grmi1440.pfb) = %{tl_version}
Provides:       tex(grmi1728.pfb) = %{tl_version}, tex(grmi2074.pfb) = %{tl_version}
Provides:       tex(grmi2488.pfb) = %{tl_version}, tex(grmi2986.pfb) = %{tl_version}
Provides:       tex(grmi3583.pfb) = %{tl_version}, tex(grml0500.pfb) = %{tl_version}
Provides:       tex(grml0600.pfb) = %{tl_version}, tex(grml0700.pfb) = %{tl_version}
Provides:       tex(grml0800.pfb) = %{tl_version}, tex(grml0900.pfb) = %{tl_version}
Provides:       tex(grml1000.pfb) = %{tl_version}, tex(grml1095.pfb) = %{tl_version}
Provides:       tex(grml1200.pfb) = %{tl_version}, tex(grml1440.pfb) = %{tl_version}
Provides:       tex(grml1728.pfb) = %{tl_version}, tex(grml2074.pfb) = %{tl_version}
Provides:       tex(grml2488.pfb) = %{tl_version}, tex(grml2986.pfb) = %{tl_version}
Provides:       tex(grml3583.pfb) = %{tl_version}, tex(grmn0500.pfb) = %{tl_version}
Provides:       tex(grmn0600.pfb) = %{tl_version}, tex(grmn0700.pfb) = %{tl_version}
Provides:       tex(grmn0800.pfb) = %{tl_version}, tex(grmn0900.pfb) = %{tl_version}
Provides:       tex(grmn1000.pfb) = %{tl_version}, tex(grmn1095.pfb) = %{tl_version}
Provides:       tex(grmn1200.pfb) = %{tl_version}, tex(grmn1440.pfb) = %{tl_version}
Provides:       tex(grmn1728.pfb) = %{tl_version}, tex(grmn2074.pfb) = %{tl_version}
Provides:       tex(grmn2488.pfb) = %{tl_version}, tex(grmn2986.pfb) = %{tl_version}
Provides:       tex(grmn3583.pfb) = %{tl_version}, tex(grmo0500.pfb) = %{tl_version}
Provides:       tex(grmo0600.pfb) = %{tl_version}, tex(grmo0700.pfb) = %{tl_version}
Provides:       tex(grmo0800.pfb) = %{tl_version}, tex(grmo0900.pfb) = %{tl_version}
Provides:       tex(grmo1000.pfb) = %{tl_version}, tex(grmo1095.pfb) = %{tl_version}
Provides:       tex(grmo1200.pfb) = %{tl_version}, tex(grmo1440.pfb) = %{tl_version}
Provides:       tex(grmo1728.pfb) = %{tl_version}, tex(grmo2074.pfb) = %{tl_version}
Provides:       tex(grmo2488.pfb) = %{tl_version}, tex(grmo2986.pfb) = %{tl_version}
Provides:       tex(grmo3583.pfb) = %{tl_version}, tex(grmu0500.pfb) = %{tl_version}
Provides:       tex(grmu0600.pfb) = %{tl_version}, tex(grmu0700.pfb) = %{tl_version}
Provides:       tex(grmu0800.pfb) = %{tl_version}, tex(grmu0900.pfb) = %{tl_version}
Provides:       tex(grmu1000.pfb) = %{tl_version}, tex(grmu1095.pfb) = %{tl_version}
Provides:       tex(grmu1200.pfb) = %{tl_version}, tex(grmu1440.pfb) = %{tl_version}
Provides:       tex(grmu1728.pfb) = %{tl_version}, tex(grmu2074.pfb) = %{tl_version}
Provides:       tex(grmu2488.pfb) = %{tl_version}, tex(grmu2986.pfb) = %{tl_version}
Provides:       tex(grmu3583.pfb) = %{tl_version}, tex(grxc0500.pfb) = %{tl_version}
Provides:       tex(grxc0600.pfb) = %{tl_version}, tex(grxc0700.pfb) = %{tl_version}
Provides:       tex(grxc0800.pfb) = %{tl_version}, tex(grxc0900.pfb) = %{tl_version}
Provides:       tex(grxc1000.pfb) = %{tl_version}, tex(grxc1095.pfb) = %{tl_version}
Provides:       tex(grxc1200.pfb) = %{tl_version}, tex(grxc1440.pfb) = %{tl_version}
Provides:       tex(grxc1728.pfb) = %{tl_version}, tex(grxc2074.pfb) = %{tl_version}
Provides:       tex(grxc2488.pfb) = %{tl_version}, tex(grxc2986.pfb) = %{tl_version}
Provides:       tex(grxc3583.pfb) = %{tl_version}, tex(grxi0500.pfb) = %{tl_version}
Provides:       tex(grxi0600.pfb) = %{tl_version}, tex(grxi0700.pfb) = %{tl_version}
Provides:       tex(grxi0800.pfb) = %{tl_version}, tex(grxi0900.pfb) = %{tl_version}
Provides:       tex(grxi1000.pfb) = %{tl_version}, tex(grxi1095.pfb) = %{tl_version}
Provides:       tex(grxi1200.pfb) = %{tl_version}, tex(grxi1440.pfb) = %{tl_version}
Provides:       tex(grxi1728.pfb) = %{tl_version}, tex(grxi2074.pfb) = %{tl_version}
Provides:       tex(grxi2488.pfb) = %{tl_version}, tex(grxi2986.pfb) = %{tl_version}
Provides:       tex(grxi3583.pfb) = %{tl_version}, tex(grxl0500.pfb) = %{tl_version}
Provides:       tex(grxl0600.pfb) = %{tl_version}, tex(grxl0700.pfb) = %{tl_version}
Provides:       tex(grxl0800.pfb) = %{tl_version}, tex(grxl0900.pfb) = %{tl_version}
Provides:       tex(grxl1000.pfb) = %{tl_version}, tex(grxl1095.pfb) = %{tl_version}
Provides:       tex(grxl1200.pfb) = %{tl_version}, tex(grxl1440.pfb) = %{tl_version}
Provides:       tex(grxl1728.pfb) = %{tl_version}, tex(grxl2074.pfb) = %{tl_version}
Provides:       tex(grxl2488.pfb) = %{tl_version}, tex(grxl2986.pfb) = %{tl_version}
Provides:       tex(grxl3583.pfb) = %{tl_version}, tex(grxn0500.pfb) = %{tl_version}
Provides:       tex(grxn0600.pfb) = %{tl_version}, tex(grxn0700.pfb) = %{tl_version}
Provides:       tex(grxn0800.pfb) = %{tl_version}, tex(grxn0900.pfb) = %{tl_version}
Provides:       tex(grxn1000.pfb) = %{tl_version}, tex(grxn1095.pfb) = %{tl_version}
Provides:       tex(grxn1200.pfb) = %{tl_version}, tex(grxn1440.pfb) = %{tl_version}
Provides:       tex(grxn1728.pfb) = %{tl_version}, tex(grxn2074.pfb) = %{tl_version}
Provides:       tex(grxn2488.pfb) = %{tl_version}, tex(grxn2986.pfb) = %{tl_version}
Provides:       tex(grxn3583.pfb) = %{tl_version}, tex(grxo0500.pfb) = %{tl_version}
Provides:       tex(grxo0600.pfb) = %{tl_version}, tex(grxo0700.pfb) = %{tl_version}
Provides:       tex(grxo0800.pfb) = %{tl_version}, tex(grxo0900.pfb) = %{tl_version}
Provides:       tex(grxo1000.pfb) = %{tl_version}, tex(grxo1095.pfb) = %{tl_version}
Provides:       tex(grxo1200.pfb) = %{tl_version}, tex(grxo1440.pfb) = %{tl_version}
Provides:       tex(grxo1728.pfb) = %{tl_version}, tex(grxo2074.pfb) = %{tl_version}
Provides:       tex(grxo2488.pfb) = %{tl_version}, tex(grxo2986.pfb) = %{tl_version}
Provides:       tex(grxo3583.pfb) = %{tl_version}, tex(grxu0500.pfb) = %{tl_version}
Provides:       tex(grxu0600.pfb) = %{tl_version}, tex(grxu0700.pfb) = %{tl_version}
Provides:       tex(grxu0800.pfb) = %{tl_version}, tex(grxu0900.pfb) = %{tl_version}
Provides:       tex(grxu1000.pfb) = %{tl_version}, tex(grxu1095.pfb) = %{tl_version}
Provides:       tex(grxu1200.pfb) = %{tl_version}, tex(grxu1440.pfb) = %{tl_version}
Provides:       tex(grxu1728.pfb) = %{tl_version}, tex(grxu2074.pfb) = %{tl_version}
Provides:       tex(grxu2488.pfb) = %{tl_version}, tex(grxu2986.pfb) = %{tl_version}
Provides:       tex(grxu3583.pfb) = %{tl_version}, tex(gsma0500.pfb) = %{tl_version}
Provides:       tex(gsma0600.pfb) = %{tl_version}, tex(gsma0700.pfb) = %{tl_version}
Provides:       tex(gsma0800.pfb) = %{tl_version}, tex(gsma0900.pfb) = %{tl_version}
Provides:       tex(gsma1000.pfb) = %{tl_version}, tex(gsma1095.pfb) = %{tl_version}
Provides:       tex(gsma1200.pfb) = %{tl_version}, tex(gsma1440.pfb) = %{tl_version}
Provides:       tex(gsma1728.pfb) = %{tl_version}, tex(gsma2074.pfb) = %{tl_version}
Provides:       tex(gsma2488.pfb) = %{tl_version}, tex(gsma2986.pfb) = %{tl_version}
Provides:       tex(gsma3583.pfb) = %{tl_version}, tex(gsmc0500.pfb) = %{tl_version}
Provides:       tex(gsmc0600.pfb) = %{tl_version}, tex(gsmc0700.pfb) = %{tl_version}
Provides:       tex(gsmc0800.pfb) = %{tl_version}, tex(gsmc0900.pfb) = %{tl_version}
Provides:       tex(gsmc1000.pfb) = %{tl_version}, tex(gsmc1095.pfb) = %{tl_version}
Provides:       tex(gsmc1200.pfb) = %{tl_version}, tex(gsmc1440.pfb) = %{tl_version}
Provides:       tex(gsmc1728.pfb) = %{tl_version}, tex(gsmc2074.pfb) = %{tl_version}
Provides:       tex(gsmc2488.pfb) = %{tl_version}, tex(gsmc2986.pfb) = %{tl_version}
Provides:       tex(gsmc3583.pfb) = %{tl_version}, tex(gsme0500.pfb) = %{tl_version}
Provides:       tex(gsme0600.pfb) = %{tl_version}, tex(gsme0700.pfb) = %{tl_version}
Provides:       tex(gsme0800.pfb) = %{tl_version}, tex(gsme0900.pfb) = %{tl_version}
Provides:       tex(gsme1000.pfb) = %{tl_version}, tex(gsme1095.pfb) = %{tl_version}
Provides:       tex(gsme1200.pfb) = %{tl_version}, tex(gsme1440.pfb) = %{tl_version}
Provides:       tex(gsme1728.pfb) = %{tl_version}, tex(gsme2074.pfb) = %{tl_version}
Provides:       tex(gsme2488.pfb) = %{tl_version}, tex(gsme2986.pfb) = %{tl_version}
Provides:       tex(gsme3583.pfb) = %{tl_version}, tex(gsmi0500.pfb) = %{tl_version}
Provides:       tex(gsmi0600.pfb) = %{tl_version}, tex(gsmi0700.pfb) = %{tl_version}
Provides:       tex(gsmi0800.pfb) = %{tl_version}, tex(gsmi0900.pfb) = %{tl_version}
Provides:       tex(gsmi1000.pfb) = %{tl_version}, tex(gsmi1095.pfb) = %{tl_version}
Provides:       tex(gsmi1200.pfb) = %{tl_version}, tex(gsmi1440.pfb) = %{tl_version}
Provides:       tex(gsmi1728.pfb) = %{tl_version}, tex(gsmi2074.pfb) = %{tl_version}
Provides:       tex(gsmi2488.pfb) = %{tl_version}, tex(gsmi2986.pfb) = %{tl_version}
Provides:       tex(gsmi3583.pfb) = %{tl_version}, tex(gsmn0500.pfb) = %{tl_version}
Provides:       tex(gsmn0600.pfb) = %{tl_version}, tex(gsmn0700.pfb) = %{tl_version}
Provides:       tex(gsmn0800.pfb) = %{tl_version}, tex(gsmn0900.pfb) = %{tl_version}
Provides:       tex(gsmn1000.pfb) = %{tl_version}, tex(gsmn1095.pfb) = %{tl_version}
Provides:       tex(gsmn1200.pfb) = %{tl_version}, tex(gsmn1440.pfb) = %{tl_version}
Provides:       tex(gsmn1728.pfb) = %{tl_version}, tex(gsmn2074.pfb) = %{tl_version}
Provides:       tex(gsmn2488.pfb) = %{tl_version}, tex(gsmn2986.pfb) = %{tl_version}
Provides:       tex(gsmn3583.pfb) = %{tl_version}, tex(gsmo0500.pfb) = %{tl_version}
Provides:       tex(gsmo0600.pfb) = %{tl_version}, tex(gsmo0700.pfb) = %{tl_version}
Provides:       tex(gsmo0800.pfb) = %{tl_version}, tex(gsmo0900.pfb) = %{tl_version}
Provides:       tex(gsmo1000.pfb) = %{tl_version}, tex(gsmo1095.pfb) = %{tl_version}
Provides:       tex(gsmo1200.pfb) = %{tl_version}, tex(gsmo1440.pfb) = %{tl_version}
Provides:       tex(gsmo1728.pfb) = %{tl_version}, tex(gsmo2074.pfb) = %{tl_version}
Provides:       tex(gsmo2488.pfb) = %{tl_version}, tex(gsmo2986.pfb) = %{tl_version}
Provides:       tex(gsmo3583.pfb) = %{tl_version}, tex(gsmu0500.pfb) = %{tl_version}
Provides:       tex(gsmu0600.pfb) = %{tl_version}, tex(gsmu0700.pfb) = %{tl_version}
Provides:       tex(gsmu0800.pfb) = %{tl_version}, tex(gsmu0900.pfb) = %{tl_version}
Provides:       tex(gsmu1000.pfb) = %{tl_version}, tex(gsmu1095.pfb) = %{tl_version}
Provides:       tex(gsmu1200.pfb) = %{tl_version}, tex(gsmu1440.pfb) = %{tl_version}
Provides:       tex(gsmu1728.pfb) = %{tl_version}, tex(gsmu2074.pfb) = %{tl_version}
Provides:       tex(gsmu2488.pfb) = %{tl_version}, tex(gsmu2986.pfb) = %{tl_version}
Provides:       tex(gsmu3583.pfb) = %{tl_version}, tex(gsxa0500.pfb) = %{tl_version}
Provides:       tex(gsxa0600.pfb) = %{tl_version}, tex(gsxa0700.pfb) = %{tl_version}
Provides:       tex(gsxa0800.pfb) = %{tl_version}, tex(gsxa0900.pfb) = %{tl_version}
Provides:       tex(gsxa1000.pfb) = %{tl_version}, tex(gsxa1095.pfb) = %{tl_version}
Provides:       tex(gsxa1200.pfb) = %{tl_version}, tex(gsxa1440.pfb) = %{tl_version}
Provides:       tex(gsxa1728.pfb) = %{tl_version}, tex(gsxa2074.pfb) = %{tl_version}
Provides:       tex(gsxa2488.pfb) = %{tl_version}, tex(gsxa2986.pfb) = %{tl_version}
Provides:       tex(gsxa3583.pfb) = %{tl_version}, tex(gsxc0500.pfb) = %{tl_version}
Provides:       tex(gsxc0600.pfb) = %{tl_version}, tex(gsxc0700.pfb) = %{tl_version}
Provides:       tex(gsxc0800.pfb) = %{tl_version}, tex(gsxc0900.pfb) = %{tl_version}
Provides:       tex(gsxc1000.pfb) = %{tl_version}, tex(gsxc1095.pfb) = %{tl_version}
Provides:       tex(gsxc1200.pfb) = %{tl_version}, tex(gsxc1440.pfb) = %{tl_version}
Provides:       tex(gsxc1728.pfb) = %{tl_version}, tex(gsxc2074.pfb) = %{tl_version}
Provides:       tex(gsxc2488.pfb) = %{tl_version}, tex(gsxc2986.pfb) = %{tl_version}
Provides:       tex(gsxc3583.pfb) = %{tl_version}, tex(gsxe0500.pfb) = %{tl_version}
Provides:       tex(gsxe0600.pfb) = %{tl_version}, tex(gsxe0700.pfb) = %{tl_version}
Provides:       tex(gsxe0800.pfb) = %{tl_version}, tex(gsxe0900.pfb) = %{tl_version}
Provides:       tex(gsxe1000.pfb) = %{tl_version}, tex(gsxe1095.pfb) = %{tl_version}
Provides:       tex(gsxe1200.pfb) = %{tl_version}, tex(gsxe1440.pfb) = %{tl_version}
Provides:       tex(gsxe1728.pfb) = %{tl_version}, tex(gsxe2074.pfb) = %{tl_version}
Provides:       tex(gsxe2488.pfb) = %{tl_version}, tex(gsxe2986.pfb) = %{tl_version}
Provides:       tex(gsxe3583.pfb) = %{tl_version}, tex(gsxi0500.pfb) = %{tl_version}
Provides:       tex(gsxi0600.pfb) = %{tl_version}, tex(gsxi0700.pfb) = %{tl_version}
Provides:       tex(gsxi0800.pfb) = %{tl_version}, tex(gsxi0900.pfb) = %{tl_version}
Provides:       tex(gsxi1000.pfb) = %{tl_version}, tex(gsxi1095.pfb) = %{tl_version}
Provides:       tex(gsxi1200.pfb) = %{tl_version}, tex(gsxi1440.pfb) = %{tl_version}
Provides:       tex(gsxi1728.pfb) = %{tl_version}, tex(gsxi2074.pfb) = %{tl_version}
Provides:       tex(gsxi2488.pfb) = %{tl_version}, tex(gsxi2986.pfb) = %{tl_version}
Provides:       tex(gsxi3583.pfb) = %{tl_version}, tex(gsxn0500.pfb) = %{tl_version}
Provides:       tex(gsxn0600.pfb) = %{tl_version}, tex(gsxn0700.pfb) = %{tl_version}
Provides:       tex(gsxn0800.pfb) = %{tl_version}, tex(gsxn0900.pfb) = %{tl_version}
Provides:       tex(gsxn1000.pfb) = %{tl_version}, tex(gsxn1095.pfb) = %{tl_version}
Provides:       tex(gsxn1200.pfb) = %{tl_version}, tex(gsxn1440.pfb) = %{tl_version}
Provides:       tex(gsxn1728.pfb) = %{tl_version}, tex(gsxn2074.pfb) = %{tl_version}
Provides:       tex(gsxn2488.pfb) = %{tl_version}, tex(gsxn2986.pfb) = %{tl_version}
Provides:       tex(gsxn3583.pfb) = %{tl_version}, tex(gsxo0500.pfb) = %{tl_version}
Provides:       tex(gsxo0600.pfb) = %{tl_version}, tex(gsxo0700.pfb) = %{tl_version}
Provides:       tex(gsxo0800.pfb) = %{tl_version}, tex(gsxo0900.pfb) = %{tl_version}
Provides:       tex(gsxo1000.pfb) = %{tl_version}, tex(gsxo1095.pfb) = %{tl_version}
Provides:       tex(gsxo1200.pfb) = %{tl_version}, tex(gsxo1440.pfb) = %{tl_version}
Provides:       tex(gsxo1728.pfb) = %{tl_version}, tex(gsxo2074.pfb) = %{tl_version}
Provides:       tex(gsxo2488.pfb) = %{tl_version}, tex(gsxo2986.pfb) = %{tl_version}
Provides:       tex(gsxo3583.pfb) = %{tl_version}, tex(gsxu0500.pfb) = %{tl_version}
Provides:       tex(gsxu0600.pfb) = %{tl_version}, tex(gsxu0700.pfb) = %{tl_version}
Provides:       tex(gsxu0800.pfb) = %{tl_version}, tex(gsxu0900.pfb) = %{tl_version}
Provides:       tex(gsxu1000.pfb) = %{tl_version}, tex(gsxu1095.pfb) = %{tl_version}
Provides:       tex(gsxu1200.pfb) = %{tl_version}, tex(gsxu1440.pfb) = %{tl_version}
Provides:       tex(gsxu1728.pfb) = %{tl_version}, tex(gsxu2074.pfb) = %{tl_version}
Provides:       tex(gsxu2488.pfb) = %{tl_version}, tex(gsxu2986.pfb) = %{tl_version}
Provides:       tex(gsxu3583.pfb) = %{tl_version}, tex(gttc0500.pfb) = %{tl_version}
Provides:       tex(gttc0600.pfb) = %{tl_version}, tex(gttc0700.pfb) = %{tl_version}
Provides:       tex(gttc0800.pfb) = %{tl_version}, tex(gttc0900.pfb) = %{tl_version}
Provides:       tex(gttc1000.pfb) = %{tl_version}, tex(gttc1095.pfb) = %{tl_version}
Provides:       tex(gttc1200.pfb) = %{tl_version}, tex(gttc1440.pfb) = %{tl_version}
Provides:       tex(gttc1728.pfb) = %{tl_version}, tex(gttc2074.pfb) = %{tl_version}
Provides:       tex(gttc2488.pfb) = %{tl_version}, tex(gttc2986.pfb) = %{tl_version}
Provides:       tex(gttc3583.pfb) = %{tl_version}, tex(gtti0500.pfb) = %{tl_version}
Provides:       tex(gtti0600.pfb) = %{tl_version}, tex(gtti0700.pfb) = %{tl_version}
Provides:       tex(gtti0800.pfb) = %{tl_version}, tex(gtti0900.pfb) = %{tl_version}
Provides:       tex(gtti1000.pfb) = %{tl_version}, tex(gtti1095.pfb) = %{tl_version}
Provides:       tex(gtti1200.pfb) = %{tl_version}, tex(gtti1440.pfb) = %{tl_version}
Provides:       tex(gtti1728.pfb) = %{tl_version}, tex(gtti2074.pfb) = %{tl_version}
Provides:       tex(gtti2488.pfb) = %{tl_version}, tex(gtti2986.pfb) = %{tl_version}
Provides:       tex(gtti3583.pfb) = %{tl_version}, tex(gttn0500.pfb) = %{tl_version}
Provides:       tex(gttn0600.pfb) = %{tl_version}, tex(gttn0700.pfb) = %{tl_version}
Provides:       tex(gttn0800.pfb) = %{tl_version}, tex(gttn0900.pfb) = %{tl_version}
Provides:       tex(gttn1000.pfb) = %{tl_version}, tex(gttn1095.pfb) = %{tl_version}
Provides:       tex(gttn1200.pfb) = %{tl_version}, tex(gttn1440.pfb) = %{tl_version}
Provides:       tex(gttn1728.pfb) = %{tl_version}, tex(gttn2074.pfb) = %{tl_version}
Provides:       tex(gttn2488.pfb) = %{tl_version}, tex(gttn2986.pfb) = %{tl_version}
Provides:       tex(gttn3583.pfb) = %{tl_version}, tex(gtto0500.pfb) = %{tl_version}
Provides:       tex(gtto0600.pfb) = %{tl_version}, tex(gtto0700.pfb) = %{tl_version}
Provides:       tex(gtto0800.pfb) = %{tl_version}, tex(gtto0900.pfb) = %{tl_version}
Provides:       tex(gtto1000.pfb) = %{tl_version}, tex(gtto1095.pfb) = %{tl_version}
Provides:       tex(gtto1200.pfb) = %{tl_version}, tex(gtto1440.pfb) = %{tl_version}
Provides:       tex(gtto1728.pfb) = %{tl_version}, tex(gtto2074.pfb) = %{tl_version}
Provides:       tex(gtto2488.pfb) = %{tl_version}, tex(gtto2986.pfb) = %{tl_version}
Provides:       tex(gtto3583.pfb) = %{tl_version}, tex(gttu0500.pfb) = %{tl_version}
Provides:       tex(gttu0600.pfb) = %{tl_version}, tex(gttu0700.pfb) = %{tl_version}
Provides:       tex(gttu0800.pfb) = %{tl_version}, tex(gttu0900.pfb) = %{tl_version}
Provides:       tex(gttu1000.pfb) = %{tl_version}, tex(gttu1095.pfb) = %{tl_version}
Provides:       tex(gttu1200.pfb) = %{tl_version}, tex(gttu1440.pfb) = %{tl_version}
Provides:       tex(gttu1728.pfb) = %{tl_version}, tex(gttu2074.pfb) = %{tl_version}
Provides:       tex(gttu2488.pfb) = %{tl_version}, tex(gttu2986.pfb) = %{tl_version}
Provides:       tex(gttu3583.pfb) = %{tl_version}

%description -n texlive-cbfonts
This bundle presents the whole of Beccari's original Greek font
set, which use the 'Lispiakos' font shape derived from the
shape of the fonts used in printers' shops in Lispia. The fonts
are available both as Metafont source and in Adobe Type 1
format, and at the same wide set of design sizes as are such
font sets as the EC fonts.

%package -n texlive-cbfonts-doc
Summary:        Documentation for cbfonts
Version:        svn31624.0

Provides:       tex-cbfonts-doc
AutoReqProv:    No
Requires:       tex-cbfonts-fd-doc

%description -n texlive-cbfonts-doc
Documentation for cbfonts

%package -n texlive-ccaption
Provides:       tex-ccaption = %{tl_version}
License:        LPPL 1.3
Summary:        Continuation headings and legends for floats
Version:        svn23443.3.2c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ccaption.sty) = %{tl_version}

%description -n texlive-ccaption
A package providing commands for 'continuation captions',
unnumbered captions, and also a non-specific legend heading for
any environment. Methods are also provided to define captions
for use outside float (e.g., figure and table) environments,
and to define new float environments and Lists of Floats. Tools
are provided for specifying your own captioning styles.

%package -n texlive-ccaption-doc
Summary:        Documentation for ccaption
Version:        svn23443.3.2c

Provides:       tex-ccaption-doc
AutoReqProv:    No

%description -n texlive-ccaption-doc
Documentation for ccaption

%package -n texlive-ccfonts
Provides:       tex-ccfonts = %{tl_version}
License:        LPPL
Summary:        Support for Concrete text and math fonts in LaTeX
Version:        svn17122.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(ccfonts.sty) = %{tl_version}, tex(t1ccr.fd) = %{tl_version}
Provides:       tex(ts1ccr.fd) = %{tl_version}

%description -n texlive-ccfonts
LaTeX font definition files for the Concrete fonts and a LaTeX
package for typesetting documents using Concrete as the default
font family. The files support OT1, T1, TS1, and Concrete
mathematics including AMS fonts (Ulrik Vieth's concmath).

%package -n texlive-ccfonts-doc
Summary:        Documentation for ccfonts
Version:        svn17122.1.1

Provides:       tex-ccfonts-doc
AutoReqProv:    No

%description -n texlive-ccfonts-doc
Documentation for ccfonts

%package -n texlive-ccicons
Provides:       tex-ccicons = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX support for Creative Commons icons
Version:        svn45646
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex, tex(xkeyval.sty)
Provides:       tex(ccicons-u.enc) = %{tl_version}, tex(ccicons.map) = %{tl_version}
Provides:       tex(ccicons.otf) = %{tl_version}, tex(ccicons.tfm) = %{tl_version}
Provides:       tex(ccicons.pfb) = %{tl_version}, tex(ccicons.sty) = %{tl_version}

%description -n texlive-ccicons
The package provides the means to typeset Creative Commons
icons, in documents licensed under CC licences. A font (in
Adobe Type 1 format) and LaTeX support macros are provided.

%package -n texlive-ccicons-doc
Summary:        Documentation for ccicons
Version:        svn45646
Provides:       tex-ccicons-doc
AutoReqProv:    No

%description -n texlive-ccicons-doc
Documentation for ccicons

%package -n texlive-cclicenses
Provides:       tex-cclicenses = %{tl_version}
License:        LPPL
Summary:        Typeset Creative Commons licence logos
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(rotating.sty)
Provides:       tex(cclicenses.sty) = %{tl_version}

%description -n texlive-cclicenses
The cclicenses package helps users typesetting Creative Commons
logos in LaTeX. It defines some commands useful to quickly
write these logos, related to CC licences versions 1.0 and 2.0.

%package -n texlive-cclicenses-doc
Summary:        Documentation for cclicenses
Version:        svn15878.0

Provides:       tex-cclicenses-doc
AutoReqProv:    No

%description -n texlive-cclicenses-doc
Documentation for cclicenses

%package -n texlive-cc-pl
Provides:       tex-cc-pl = %{tl_version}
License:        Public Domain
Summary:        Polish extension of Computer Concrete fonts
Version:        svn15878.1.02.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(ccpl.map) = %{tl_version}, tex(pccsc10.tfm) = %{tl_version}
Provides:       tex(pcmi10.tfm) = %{tl_version}, tex(pcr10.tfm) = %{tl_version}
Provides:       tex(pcr5.tfm) = %{tl_version}, tex(pcr6.tfm) = %{tl_version}
Provides:       tex(pcr7.tfm) = %{tl_version}, tex(pcr8.tfm) = %{tl_version}
Provides:       tex(pcr9.tfm) = %{tl_version}, tex(pcsl10.tfm) = %{tl_version}
Provides:       tex(pcslc9.tfm) = %{tl_version}, tex(pcti10.tfm) = %{tl_version}
Provides:       tex(pccsc10.pfb) = %{tl_version}, tex(pcmi10.pfb) = %{tl_version}
Provides:       tex(pcr10.pfb) = %{tl_version}, tex(pcr5.pfb) = %{tl_version}
Provides:       tex(pcr6.pfb) = %{tl_version}, tex(pcr7.pfb) = %{tl_version}
Provides:       tex(pcr8.pfb) = %{tl_version}, tex(pcr9.pfb) = %{tl_version}
Provides:       tex(pcsl10.pfb) = %{tl_version}, tex(pcslc9.pfb) = %{tl_version}
Provides:       tex(pcti10.pfb) = %{tl_version}

%description -n texlive-cc-pl
These Metafont sources rely on the availability of the Metafont
'Polish' fonts and of the Metafont sources of the original
Concrete fonts. Adobe Type 1 versions of the fonts are
included.

%package -n texlive-cc-pl-doc
Summary:        Documentation for cc-pl
Version:        svn15878.1.02.2

Provides:       tex-cc-pl-doc
AutoReqProv:    No

%description -n texlive-cc-pl-doc
Documentation for cc-pl

%package -n texlive-cd-cover
Provides:       tex-cd-cover = %{tl_version}
License:        GPL+
Summary:        Typeset CD covers
Version:        svn17121.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(rotating.sty)
Provides:       tex(cd-cover.cls) = %{tl_version}

%description -n texlive-cd-cover
The CD-cover class will typeset front and back cover sheets for
CD jewel cases, or an entire paper cover, or a label for a
plastic slip-cover.

%package -n texlive-cd-cover-doc
Summary:        Documentation for cd-cover
Version:        svn17121.1.0

Provides:       tex-cd-cover-doc
AutoReqProv:    No

%description -n texlive-cd-cover-doc
Documentation for cd-cover

%package -n texlive-cdpbundl
Provides:       tex-cdpbundl = %{tl_version}
License:        LPPL
Summary:        Business letters in the Italian style
Version:        svn46613
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(color.sty), tex(hyperref.sty), tex(babel.sty), tex(eepic.sty)
Provides:       tex(articoletteracdp.cls) = %{tl_version}
Provides:       tex(cdpaddon.sty) = %{tl_version}, tex(cdpbabel.sty) = %{tl_version}
Provides:       tex(cdpnamesenglish.ldf) = %{tl_version}
Provides:       tex(cdpnamesitalian.ldf) = %{tl_version}
Provides:       tex(cdpshues-example.def) = %{tl_version}
Provides:       tex(cdpshues.cfg) = %{tl_version}, tex(epson-stylus-740.def) = %{tl_version}
Provides:       tex(hp-laserjet-4500.def) = %{tl_version}
Provides:       tex(letteracdp.cls) = %{tl_version}

%description -n texlive-cdpbundl
The C.D.P. Bundle can be used to typeset high-quality business
letters formatted according to Italian style conventions. It is
highly configurable, and its modular structure provides you
with building blocks of increasing level, by means of which you
can compose a large variety of letters. It is also possible to
write letters divided into sections and paragraphs, to include
floating figures and tables, and to have the relevant indexes
compiled automatically. A single input file can contain several
letters, and each letter will have its own table of contents,
etc., independant from the other ones.

%package -n texlive-cdpbundl-doc
Summary:        Documentation for cdpbundl
Version:        svn46613
Provides:       tex-cdpbundl-doc
AutoReqProv:    No

%description -n texlive-cdpbundl-doc
Documentation for cdpbundl

%package -n texlive-cd
Provides:       tex-cd = %{tl_version}
License:        GPL+
Summary:        Typeset CD covers
Version:        svn34452.1.4

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(rotating.sty)
Provides:       tex(cd.cls) = %{tl_version}

%description -n texlive-cd
Normal usage will ordinarily require no more than a simple data
file per cover; the package will make a full insert for a CD
case (it copes with both normal and slim cases).

%package -n texlive-cd-doc
Summary:        Documentation for cd
Version:        svn34452.1.4

Provides:       tex-cd-doc
AutoReqProv:    No

%description -n texlive-cd-doc
Documentation for cd

%package -n texlive-cellspace
Provides:       tex-cellspace = %{tl_version}
License:        LPPL
Summary:        Ensure minimal spacing of table cells
Version:        svn45034
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(ifthen.sty), tex(array.sty), tex(calc.sty), tex(amsmath.sty)
Provides:       tex(cellspace.sty) = %{tl_version}

%description -n texlive-cellspace
It is well known that high or deep cells tend to touch the
\hlines of a tabular. This package provides a modifier S acting
on usual column types so that to ensure a minimal distance that
can be controlled through two parameters \cellspacetoplimit and
\cellspacebottomlimit. The approach employed by this package is
noticeably simpler than that of tabls, which considers the
dimensions of each entire row; whereas you can ask the
cellspace only to look at the cells of potentially difficult
columns.

%package -n texlive-cellspace-doc
Summary:        Documentation for cellspace
Version:        svn45034
Provides:       tex-cellspace-doc
AutoReqProv:    No

%description -n texlive-cellspace-doc
Documentation for cellspace

%package -n texlive-cell
Provides:       tex-cell = %{tl_version}
License:        Public Domain
Summary:        Bibliography style for Cell
Version:        svn42428
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(cite.sty)
Provides:       tex(cell.sty) = %{tl_version}

%description -n texlive-cell
This is an "apa-like" style (cf. apalike.bst in the BibTeX
distribution), developed from the same author's JMB style. A
supporting LaTeX package is also provided.

%package -n texlive-cell-doc
Summary:        Documentation for cell
Version:        svn42428
Provides:       tex-cell-doc
AutoReqProv:    No

%description -n texlive-cell-doc
Documentation for cell

%package -n texlive-celtic
Provides:       tex-celtic = %{tl_version}
License:        LPPL 1.3
Summary:        A TikZ library for drawing celtic knots
Version:        svn39797

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(tikzlibraryceltic.code.tex) = %{tl_version}

%description -n texlive-celtic
The package provides a TikZ library for drawing celtic knots.

%package -n texlive-celtic-doc
Summary:        Documentation for celtic
Version:        svn39797

Provides:       tex-celtic-doc
AutoReqProv:    No

%description -n texlive-celtic-doc
Documentation for celtic

%package -n texlive-censor
Provides:       tex-censor = %{tl_version}
License:        LPPL 1.3
Summary:        Facilities for controlling restricted text in a document
Version:        svn31332.3.21

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(censor.sty) = %{tl_version}

%description -n texlive-censor
The package allows a convenient redaction/censor capability to
be employed, for those who need to protect restricted
information, etc. The package can "redact" anything that can be
enclosed by a LaTeX box.

%package -n texlive-censor-doc
Summary:        Documentation for censor
Version:        svn31332.3.21

Provides:       tex-censor-doc
AutoReqProv:    No

%description -n texlive-censor-doc
Documentation for censor

%package -n texlive-cfr-initials
Provides:       tex-cfr-initials = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX packages for use of initials
Version:        svn36728.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(Acorn.fd), tex(AnnSton.fd), tex(ArtNouv.fd), tex(ArtNouvc.fd)
Requires:       tex(Carrickc.fd), tex(Eichenla.fd), tex(Eileen.fd), tex(EileenBl.fd)
Requires:       tex(Elzevier.fd), tex(GotIn.fd), tex(GoudyIn.fd), tex(Kinigcap.fd)
Requires:       tex(Konanur.fd), tex(Kramer.fd), tex(MorrisIn.fd), tex(Nouveaud.fd)
Requires:       tex(Romantik.fd), tex(Rothdn.fd), tex(RoyalIn.fd), tex(Sanremo.fd)
Requires:       tex(Starburst.fd), tex(Typocaps.fd), tex(Zallman.fd)
Provides:       tex(Acorn.sty) = %{tl_version}, tex(AnnSton.sty) = %{tl_version}
Provides:       tex(ArtNouv.sty) = %{tl_version}, tex(ArtNouvc.sty) = %{tl_version}
Provides:       tex(Carrickc.sty) = %{tl_version}, tex(Eichenla.sty) = %{tl_version}
Provides:       tex(Eileen.sty) = %{tl_version}, tex(EileenBl.sty) = %{tl_version}
Provides:       tex(Elzevier.sty) = %{tl_version}, tex(GotIn.sty) = %{tl_version}
Provides:       tex(GoudyIn.sty) = %{tl_version}, tex(Kinigcap.sty) = %{tl_version}
Provides:       tex(Konanur.sty) = %{tl_version}, tex(Kramer.sty) = %{tl_version}
Provides:       tex(MorrisIn.sty) = %{tl_version}, tex(Nouveaud.sty) = %{tl_version}
Provides:       tex(Romantik.sty) = %{tl_version}, tex(Rothdn.sty) = %{tl_version}
Provides:       tex(Royal.sty) = %{tl_version}, tex(Sanremo.sty) = %{tl_version}
Provides:       tex(Starburst.sty) = %{tl_version}, tex(Typocaps.sty) = %{tl_version}
Provides:       tex(Zallman.sty) = %{tl_version}

%description -n texlive-cfr-initials
This is a set of 23 tiny packages designed to make it easier to
use fonts from the initials package in LaTeX, e.g. with the
lettrine package. It is a response to comments on an answer at
TeX Stack Exchange (http://tex.stackexchange.com/a/236410/)
requesting sample package files for others to copy. I had
previously assumed these were too trivial to be of interest,
but if they would be useful, then I would prefer them to be
generally available via CTAN.

%package -n texlive-cfr-initials-doc
Summary:        Documentation for cfr-initials
Version:        svn36728.1.01

Provides:       tex-cfr-initials-doc
AutoReqProv:    No

%description -n texlive-cfr-initials-doc
Documentation for cfr-initials

%package -n texlive-cfr-lm
Provides:       tex-cfr-lm = %{tl_version}
License:        LPPL 1.3
Summary:        Enhanced support for the Latin Modern fonts
Version:        svn36195.1.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(xkeyval.sty), tex(fontenc.sty), tex(textcomp.sty), tex(nfssext-cfr.sty)
Provides:       tex(dotdigits-clm.enc) = %{tl_version}, tex(t1-clm.enc) = %{tl_version}
Provides:       tex(clm.map) = %{tl_version}, tex(clmb28t10.tfm) = %{tl_version}
Provides:       tex(clmb2j8t10.tfm) = %{tl_version}, tex(clmb2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmb2o8t10.tfm) = %{tl_version}, tex(clmb8t10.tfm) = %{tl_version}
Provides:       tex(clmbj8t10.tfm) = %{tl_version}, tex(clmbjo8t10.tfm) = %{tl_version}
Provides:       tex(clmbo8t10.tfm) = %{tl_version}, tex(clmbx28t10.tfm) = %{tl_version}
Provides:       tex(clmbx28t12.tfm) = %{tl_version}, tex(clmbx28t5.tfm) = %{tl_version}
Provides:       tex(clmbx28t6.tfm) = %{tl_version}, tex(clmbx28t7.tfm) = %{tl_version}
Provides:       tex(clmbx28t8.tfm) = %{tl_version}, tex(clmbx28t9.tfm) = %{tl_version}
Provides:       tex(clmbx2i8t10.tfm) = %{tl_version}, tex(clmbx2ij8t10.tfm) = %{tl_version}
Provides:       tex(clmbx2j8t10.tfm) = %{tl_version}, tex(clmbx2j8t12.tfm) = %{tl_version}
Provides:       tex(clmbx2j8t5.tfm) = %{tl_version}, tex(clmbx2j8t6.tfm) = %{tl_version}
Provides:       tex(clmbx2j8t7.tfm) = %{tl_version}, tex(clmbx2j8t8.tfm) = %{tl_version}
Provides:       tex(clmbx2j8t9.tfm) = %{tl_version}, tex(clmbx2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmbx2o8t10.tfm) = %{tl_version}, tex(clmbx8t10.tfm) = %{tl_version}
Provides:       tex(clmbx8t12.tfm) = %{tl_version}, tex(clmbx8t5.tfm) = %{tl_version}
Provides:       tex(clmbx8t6.tfm) = %{tl_version}, tex(clmbx8t7.tfm) = %{tl_version}
Provides:       tex(clmbx8t8.tfm) = %{tl_version}, tex(clmbx8t9.tfm) = %{tl_version}
Provides:       tex(clmbxi8t10.tfm) = %{tl_version}, tex(clmbxj8t10.tfm) = %{tl_version}
Provides:       tex(clmbxj8t12.tfm) = %{tl_version}, tex(clmbxj8t5.tfm) = %{tl_version}
Provides:       tex(clmbxj8t6.tfm) = %{tl_version}, tex(clmbxj8t7.tfm) = %{tl_version}
Provides:       tex(clmbxj8t8.tfm) = %{tl_version}, tex(clmbxj8t9.tfm) = %{tl_version}
Provides:       tex(clmbxji8t10.tfm) = %{tl_version}, tex(clmbxjo8t10.tfm) = %{tl_version}
Provides:       tex(clmbxo8t10.tfm) = %{tl_version}, tex(clmcsc28t10.tfm) = %{tl_version}
Provides:       tex(clmcsc2j8t10.tfm) = %{tl_version}, tex(clmcsc2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmcsc2o8t10.tfm) = %{tl_version}, tex(clmcsc8t10.tfm) = %{tl_version}
Provides:       tex(clmcscj8t10.tfm) = %{tl_version}, tex(clmcscjo8t10.tfm) = %{tl_version}
Provides:       tex(clmcsco8t10.tfm) = %{tl_version}, tex(clmdun2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmdun2o8t10.tfm) = %{tl_version}, tex(clmdunh28t10.tfm) = %{tl_version}
Provides:       tex(clmdunh2j8t10.tfm) = %{tl_version}, tex(clmdunh8t10.tfm) = %{tl_version}
Provides:       tex(clmdunhj8t10.tfm) = %{tl_version}, tex(clmdunjo8t10.tfm) = %{tl_version}
Provides:       tex(clmduno8t10.tfm) = %{tl_version}, tex(clmr28t10.tfm) = %{tl_version}
Provides:       tex(clmr28t12.tfm) = %{tl_version}, tex(clmr28t17.tfm) = %{tl_version}
Provides:       tex(clmr28t5.tfm) = %{tl_version}, tex(clmr28t6.tfm) = %{tl_version}
Provides:       tex(clmr28t7.tfm) = %{tl_version}, tex(clmr28t8.tfm) = %{tl_version}
Provides:       tex(clmr28t9.tfm) = %{tl_version}, tex(clmr2i8t10.tfm) = %{tl_version}
Provides:       tex(clmr2i8t12.tfm) = %{tl_version}, tex(clmr2i8t7.tfm) = %{tl_version}
Provides:       tex(clmr2i8t8.tfm) = %{tl_version}, tex(clmr2i8t9.tfm) = %{tl_version}
Provides:       tex(clmr2ij8t10.tfm) = %{tl_version}, tex(clmr2ij8t12.tfm) = %{tl_version}
Provides:       tex(clmr2ij8t7.tfm) = %{tl_version}, tex(clmr2ij8t8.tfm) = %{tl_version}
Provides:       tex(clmr2ij8t9.tfm) = %{tl_version}, tex(clmr2j8t10.tfm) = %{tl_version}
Provides:       tex(clmr2j8t12.tfm) = %{tl_version}, tex(clmr2j8t17.tfm) = %{tl_version}
Provides:       tex(clmr2j8t5.tfm) = %{tl_version}, tex(clmr2j8t6.tfm) = %{tl_version}
Provides:       tex(clmr2j8t7.tfm) = %{tl_version}, tex(clmr2j8t8.tfm) = %{tl_version}
Provides:       tex(clmr2j8t9.tfm) = %{tl_version}, tex(clmr2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmr2jo8t12.tfm) = %{tl_version}, tex(clmr2jo8t17.tfm) = %{tl_version}
Provides:       tex(clmr2jo8t8.tfm) = %{tl_version}, tex(clmr2jo8t9.tfm) = %{tl_version}
Provides:       tex(clmr2o8t10.tfm) = %{tl_version}, tex(clmr2o8t12.tfm) = %{tl_version}
Provides:       tex(clmr2o8t17.tfm) = %{tl_version}, tex(clmr2o8t8.tfm) = %{tl_version}
Provides:       tex(clmr2o8t9.tfm) = %{tl_version}, tex(clmr8t10.tfm) = %{tl_version}
Provides:       tex(clmr8t12.tfm) = %{tl_version}, tex(clmr8t17.tfm) = %{tl_version}
Provides:       tex(clmr8t5.tfm) = %{tl_version}, tex(clmr8t6.tfm) = %{tl_version}
Provides:       tex(clmr8t7.tfm) = %{tl_version}, tex(clmr8t8.tfm) = %{tl_version}
Provides:       tex(clmr8t9.tfm) = %{tl_version}, tex(clmri8t10.tfm) = %{tl_version}
Provides:       tex(clmri8t12.tfm) = %{tl_version}, tex(clmri8t7.tfm) = %{tl_version}
Provides:       tex(clmri8t8.tfm) = %{tl_version}, tex(clmri8t9.tfm) = %{tl_version}
Provides:       tex(clmrj8t10.tfm) = %{tl_version}, tex(clmrj8t12.tfm) = %{tl_version}
Provides:       tex(clmrj8t17.tfm) = %{tl_version}, tex(clmrj8t5.tfm) = %{tl_version}
Provides:       tex(clmrj8t6.tfm) = %{tl_version}, tex(clmrj8t7.tfm) = %{tl_version}
Provides:       tex(clmrj8t8.tfm) = %{tl_version}, tex(clmrj8t9.tfm) = %{tl_version}
Provides:       tex(clmrji8t10.tfm) = %{tl_version}, tex(clmrji8t12.tfm) = %{tl_version}
Provides:       tex(clmrji8t7.tfm) = %{tl_version}, tex(clmrji8t8.tfm) = %{tl_version}
Provides:       tex(clmrji8t9.tfm) = %{tl_version}, tex(clmrjo8t10.tfm) = %{tl_version}
Provides:       tex(clmrjo8t12.tfm) = %{tl_version}, tex(clmrjo8t17.tfm) = %{tl_version}
Provides:       tex(clmrjo8t8.tfm) = %{tl_version}, tex(clmrjo8t9.tfm) = %{tl_version}
Provides:       tex(clmro8t10.tfm) = %{tl_version}, tex(clmro8t12.tfm) = %{tl_version}
Provides:       tex(clmro8t17.tfm) = %{tl_version}, tex(clmro8t8.tfm) = %{tl_version}
Provides:       tex(clmro8t9.tfm) = %{tl_version}, tex(clmss28t10.tfm) = %{tl_version}
Provides:       tex(clmss28t12.tfm) = %{tl_version}, tex(clmss28t17.tfm) = %{tl_version}
Provides:       tex(clmss28t8.tfm) = %{tl_version}, tex(clmss28t9.tfm) = %{tl_version}
Provides:       tex(clmss2j8t10.tfm) = %{tl_version}, tex(clmss2j8t12.tfm) = %{tl_version}
Provides:       tex(clmss2j8t17.tfm) = %{tl_version}, tex(clmss2j8t8.tfm) = %{tl_version}
Provides:       tex(clmss2j8t9.tfm) = %{tl_version}, tex(clmss2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmss2jo8t12.tfm) = %{tl_version}, tex(clmss2jo8t17.tfm) = %{tl_version}
Provides:       tex(clmss2jo8t8.tfm) = %{tl_version}, tex(clmss2jo8t9.tfm) = %{tl_version}
Provides:       tex(clmss8t10.tfm) = %{tl_version}, tex(clmss8t12.tfm) = %{tl_version}
Provides:       tex(clmss8t17.tfm) = %{tl_version}, tex(clmss8t8.tfm) = %{tl_version}
Provides:       tex(clmss8t9.tfm) = %{tl_version}, tex(clmssb2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmssb2o8t10.tfm) = %{tl_version}, tex(clmssbjo8t10.tfm) = %{tl_version}
Provides:       tex(clmssbo8t10.tfm) = %{tl_version}, tex(clmssbx28t10.tfm) = %{tl_version}
Provides:       tex(clmssbx2j8t10.tfm) = %{tl_version}, tex(clmssbx8t10.tfm) = %{tl_version}
Provides:       tex(clmssbxj8t10.tfm) = %{tl_version}, tex(clmssd2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmssd2o8t10.tfm) = %{tl_version}, tex(clmssdc28t10.tfm) = %{tl_version}
Provides:       tex(clmssdc2j8t10.tfm) = %{tl_version}, tex(clmssdc8t10.tfm) = %{tl_version}
Provides:       tex(clmssdcj8t10.tfm) = %{tl_version}, tex(clmssdjo8t10.tfm) = %{tl_version}
Provides:       tex(clmssdo8t10.tfm) = %{tl_version}, tex(clmssj8t10.tfm) = %{tl_version}
Provides:       tex(clmssj8t12.tfm) = %{tl_version}, tex(clmssj8t17.tfm) = %{tl_version}
Provides:       tex(clmssj8t8.tfm) = %{tl_version}, tex(clmssj8t9.tfm) = %{tl_version}
Provides:       tex(clmssjo8t10.tfm) = %{tl_version}, tex(clmssjo8t12.tfm) = %{tl_version}
Provides:       tex(clmssjo8t17.tfm) = %{tl_version}, tex(clmssjo8t8.tfm) = %{tl_version}
Provides:       tex(clmssjo8t9.tfm) = %{tl_version}, tex(clmsso28t10.tfm) = %{tl_version}
Provides:       tex(clmsso28t12.tfm) = %{tl_version}, tex(clmsso28t17.tfm) = %{tl_version}
Provides:       tex(clmsso28t8.tfm) = %{tl_version}, tex(clmsso28t9.tfm) = %{tl_version}
Provides:       tex(clmsso8t10.tfm) = %{tl_version}, tex(clmsso8t12.tfm) = %{tl_version}
Provides:       tex(clmsso8t17.tfm) = %{tl_version}, tex(clmsso8t8.tfm) = %{tl_version}
Provides:       tex(clmsso8t9.tfm) = %{tl_version}, tex(clmssq28t8.tfm) = %{tl_version}
Provides:       tex(clmssq2j8t8.tfm) = %{tl_version}, tex(clmssq2jo8t8.tfm) = %{tl_version}
Provides:       tex(clmssq2o8t8.tfm) = %{tl_version}, tex(clmssq8t8.tfm) = %{tl_version}
Provides:       tex(clmssqb2jo8t8.tfm) = %{tl_version}, tex(clmssqb2o8t8.tfm) = %{tl_version}
Provides:       tex(clmssqbjo8t8.tfm) = %{tl_version}, tex(clmssqbo8t8.tfm) = %{tl_version}
Provides:       tex(clmssqbx28t8.tfm) = %{tl_version}, tex(clmssqbx2j8t8.tfm) = %{tl_version}
Provides:       tex(clmssqbx8t8.tfm) = %{tl_version}, tex(clmssqbxj8t8.tfm) = %{tl_version}
Provides:       tex(clmssqj8t8.tfm) = %{tl_version}, tex(clmssqjo8t8.tfm) = %{tl_version}
Provides:       tex(clmssqo8t8.tfm) = %{tl_version}, tex(clmtcsc8t10.tfm) = %{tl_version}
Provides:       tex(clmtcscj8t10.tfm) = %{tl_version}, tex(clmtcsjo8t10.tfm) = %{tl_version}
Provides:       tex(clmtcso8t10.tfm) = %{tl_version}, tex(clmtk8t10.tfm) = %{tl_version}
Provides:       tex(clmtkj8t10.tfm) = %{tl_version}, tex(clmtkjo8t10.tfm) = %{tl_version}
Provides:       tex(clmtko8t10.tfm) = %{tl_version}, tex(clmtl8t10.tfm) = %{tl_version}
Provides:       tex(clmtlc8t10.tfm) = %{tl_version}, tex(clmtlcj8t10.tfm) = %{tl_version}
Provides:       tex(clmtlcjo8t10.tfm) = %{tl_version}, tex(clmtlco8t10.tfm) = %{tl_version}
Provides:       tex(clmtlj8t10.tfm) = %{tl_version}, tex(clmtljo8t10.tfm) = %{tl_version}
Provides:       tex(clmtlo8t10.tfm) = %{tl_version}, tex(clmtt8t10.tfm) = %{tl_version}
Provides:       tex(clmtt8t12.tfm) = %{tl_version}, tex(clmtt8t8.tfm) = %{tl_version}
Provides:       tex(clmtt8t9.tfm) = %{tl_version}, tex(clmtti8t10.tfm) = %{tl_version}
Provides:       tex(clmttij8t10.tfm) = %{tl_version}, tex(clmttj8t10.tfm) = %{tl_version}
Provides:       tex(clmttj8t12.tfm) = %{tl_version}, tex(clmttj8t8.tfm) = %{tl_version}
Provides:       tex(clmttj8t9.tfm) = %{tl_version}, tex(clmttjo8t10.tfm) = %{tl_version}
Provides:       tex(clmtto8t10.tfm) = %{tl_version}, tex(clmu28t10.tfm) = %{tl_version}
Provides:       tex(clmu2j8t10.tfm) = %{tl_version}, tex(clmu8t10.tfm) = %{tl_version}
Provides:       tex(clmuj8t10.tfm) = %{tl_version}, tex(clmvtk28t10.tfm) = %{tl_version}
Provides:       tex(clmvtk2j8t10.tfm) = %{tl_version}, tex(clmvtk2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmvtk2o8t10.tfm) = %{tl_version}, tex(clmvtk8t10.tfm) = %{tl_version}
Provides:       tex(clmvtkj8t10.tfm) = %{tl_version}, tex(clmvtkjo8t10.tfm) = %{tl_version}
Provides:       tex(clmvtko8t10.tfm) = %{tl_version}, tex(clmvtl28t10.tfm) = %{tl_version}
Provides:       tex(clmvtl2j8t10.tfm) = %{tl_version}, tex(clmvtl2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmvtl2o8t10.tfm) = %{tl_version}, tex(clmvtl8t10.tfm) = %{tl_version}
Provides:       tex(clmvtlj8t10.tfm) = %{tl_version}, tex(clmvtljo8t10.tfm) = %{tl_version}
Provides:       tex(clmvtlo8t10.tfm) = %{tl_version}, tex(clmvtt28t10.tfm) = %{tl_version}
Provides:       tex(clmvtt2j8t10.tfm) = %{tl_version}, tex(clmvtt2jo8t10.tfm) = %{tl_version}
Provides:       tex(clmvtt2o8t10.tfm) = %{tl_version}, tex(clmvtt8t10.tfm) = %{tl_version}
Provides:       tex(clmvttj8t10.tfm) = %{tl_version}, tex(clmvttjo8t10.tfm) = %{tl_version}
Provides:       tex(clmvtto8t10.tfm) = %{tl_version}, tex(dd-lmb10.tfm) = %{tl_version}
Provides:       tex(dd-lmbo10.tfm) = %{tl_version}, tex(dd-lmbx10.tfm) = %{tl_version}
Provides:       tex(dd-lmbx12.tfm) = %{tl_version}, tex(dd-lmbx5.tfm) = %{tl_version}
Provides:       tex(dd-lmbx6.tfm) = %{tl_version}, tex(dd-lmbx7.tfm) = %{tl_version}
Provides:       tex(dd-lmbx8.tfm) = %{tl_version}, tex(dd-lmbx9.tfm) = %{tl_version}
Provides:       tex(dd-lmbxi10.tfm) = %{tl_version}, tex(dd-lmbxo10.tfm) = %{tl_version}
Provides:       tex(dd-lmcsc10.tfm) = %{tl_version}, tex(dd-lmcsco10.tfm) = %{tl_version}
Provides:       tex(dd-lmdunh10.tfm) = %{tl_version}, tex(dd-lmduno10.tfm) = %{tl_version}
Provides:       tex(dd-lmr10.tfm) = %{tl_version}, tex(dd-lmr12.tfm) = %{tl_version}
Provides:       tex(dd-lmr17.tfm) = %{tl_version}, tex(dd-lmr5.tfm) = %{tl_version}
Provides:       tex(dd-lmr6.tfm) = %{tl_version}, tex(dd-lmr7.tfm) = %{tl_version}
Provides:       tex(dd-lmr8.tfm) = %{tl_version}, tex(dd-lmr9.tfm) = %{tl_version}
Provides:       tex(dd-lmri10.tfm) = %{tl_version}, tex(dd-lmri12.tfm) = %{tl_version}
Provides:       tex(dd-lmri7.tfm) = %{tl_version}, tex(dd-lmri8.tfm) = %{tl_version}
Provides:       tex(dd-lmri9.tfm) = %{tl_version}, tex(dd-lmro10.tfm) = %{tl_version}
Provides:       tex(dd-lmro12.tfm) = %{tl_version}, tex(dd-lmro17.tfm) = %{tl_version}
Provides:       tex(dd-lmro8.tfm) = %{tl_version}, tex(dd-lmro9.tfm) = %{tl_version}
Provides:       tex(dd-lmss10.tfm) = %{tl_version}, tex(dd-lmss12.tfm) = %{tl_version}
Provides:       tex(dd-lmss17.tfm) = %{tl_version}, tex(dd-lmss8.tfm) = %{tl_version}
Provides:       tex(dd-lmss9.tfm) = %{tl_version}, tex(dd-lmssbo10.tfm) = %{tl_version}
Provides:       tex(dd-lmssbx10.tfm) = %{tl_version}, tex(dd-lmssdc10.tfm) = %{tl_version}
Provides:       tex(dd-lmssdo10.tfm) = %{tl_version}, tex(dd-lmsso10.tfm) = %{tl_version}
Provides:       tex(dd-lmsso12.tfm) = %{tl_version}, tex(dd-lmsso17.tfm) = %{tl_version}
Provides:       tex(dd-lmsso8.tfm) = %{tl_version}, tex(dd-lmsso9.tfm) = %{tl_version}
Provides:       tex(dd-lmssq8.tfm) = %{tl_version}, tex(dd-lmssqbo8.tfm) = %{tl_version}
Provides:       tex(dd-lmssqbx8.tfm) = %{tl_version}, tex(dd-lmssqo8.tfm) = %{tl_version}
Provides:       tex(dd-lmtcsc10.tfm) = %{tl_version}, tex(dd-lmtcso10.tfm) = %{tl_version}
Provides:       tex(dd-lmtk10.tfm) = %{tl_version}, tex(dd-lmtko10.tfm) = %{tl_version}
Provides:       tex(dd-lmtl10.tfm) = %{tl_version}, tex(dd-lmtlc10.tfm) = %{tl_version}
Provides:       tex(dd-lmtlco10.tfm) = %{tl_version}, tex(dd-lmtlo10.tfm) = %{tl_version}
Provides:       tex(dd-lmtt10.tfm) = %{tl_version}, tex(dd-lmtt12.tfm) = %{tl_version}
Provides:       tex(dd-lmtt8.tfm) = %{tl_version}, tex(dd-lmtt9.tfm) = %{tl_version}
Provides:       tex(dd-lmtti10.tfm) = %{tl_version}, tex(dd-lmtto10.tfm) = %{tl_version}
Provides:       tex(dd-lmu10.tfm) = %{tl_version}, tex(dd-lmvtk10.tfm) = %{tl_version}
Provides:       tex(dd-lmvtko10.tfm) = %{tl_version}, tex(dd-lmvtl10.tfm) = %{tl_version}
Provides:       tex(dd-lmvtlo10.tfm) = %{tl_version}, tex(dd-lmvtt10.tfm) = %{tl_version}
Provides:       tex(dd-lmvtto10.tfm) = %{tl_version}, tex(lmb8ttl10.tfm) = %{tl_version}
Provides:       tex(lmbo8ttl10.tfm) = %{tl_version}, tex(lmbx8ttl10.tfm) = %{tl_version}
Provides:       tex(lmbx8ttl12.tfm) = %{tl_version}, tex(lmbx8ttl5.tfm) = %{tl_version}
Provides:       tex(lmbx8ttl6.tfm) = %{tl_version}, tex(lmbx8ttl7.tfm) = %{tl_version}
Provides:       tex(lmbx8ttl8.tfm) = %{tl_version}, tex(lmbx8ttl9.tfm) = %{tl_version}
Provides:       tex(lmbxi8ttl10.tfm) = %{tl_version}, tex(lmbxo8ttl10.tfm) = %{tl_version}
Provides:       tex(lmcsc8ttl10.tfm) = %{tl_version}, tex(lmcsco8ttl10.tfm) = %{tl_version}
Provides:       tex(lmdunh8ttl10.tfm) = %{tl_version}, tex(lmduno8ttl10.tfm) = %{tl_version}
Provides:       tex(lmr8ttl10.tfm) = %{tl_version}, tex(lmr8ttl12.tfm) = %{tl_version}
Provides:       tex(lmr8ttl17.tfm) = %{tl_version}, tex(lmr8ttl5.tfm) = %{tl_version}
Provides:       tex(lmr8ttl6.tfm) = %{tl_version}, tex(lmr8ttl7.tfm) = %{tl_version}
Provides:       tex(lmr8ttl8.tfm) = %{tl_version}, tex(lmr8ttl9.tfm) = %{tl_version}
Provides:       tex(lmri8ttl10.tfm) = %{tl_version}, tex(lmri8ttl12.tfm) = %{tl_version}
Provides:       tex(lmri8ttl7.tfm) = %{tl_version}, tex(lmri8ttl8.tfm) = %{tl_version}
Provides:       tex(lmri8ttl9.tfm) = %{tl_version}, tex(lmro8ttl10.tfm) = %{tl_version}
Provides:       tex(lmro8ttl12.tfm) = %{tl_version}, tex(lmro8ttl17.tfm) = %{tl_version}
Provides:       tex(lmro8ttl8.tfm) = %{tl_version}, tex(lmro8ttl9.tfm) = %{tl_version}
Provides:       tex(lmss8ttl10.tfm) = %{tl_version}, tex(lmss8ttl12.tfm) = %{tl_version}
Provides:       tex(lmss8ttl17.tfm) = %{tl_version}, tex(lmss8ttl8.tfm) = %{tl_version}
Provides:       tex(lmss8ttl9.tfm) = %{tl_version}, tex(lmssbo8ttl10.tfm) = %{tl_version}
Provides:       tex(lmssbx8ttl10.tfm) = %{tl_version}, tex(lmssdc8ttl10.tfm) = %{tl_version}
Provides:       tex(lmssdo8ttl10.tfm) = %{tl_version}, tex(lmsso8ttl10.tfm) = %{tl_version}
Provides:       tex(lmsso8ttl12.tfm) = %{tl_version}, tex(lmsso8ttl17.tfm) = %{tl_version}
Provides:       tex(lmsso8ttl8.tfm) = %{tl_version}, tex(lmsso8ttl9.tfm) = %{tl_version}
Provides:       tex(lmssq8ttl8.tfm) = %{tl_version}, tex(lmssqbo8ttl8.tfm) = %{tl_version}
Provides:       tex(lmssqbx8ttl8.tfm) = %{tl_version}, tex(lmssqo8ttl8.tfm) = %{tl_version}
Provides:       tex(lmtcsc8ttl10.tfm) = %{tl_version}, tex(lmtcso8ttl10.tfm) = %{tl_version}
Provides:       tex(lmtk8ttl10.tfm) = %{tl_version}, tex(lmtko8ttl10.tfm) = %{tl_version}
Provides:       tex(lmtl8ttl10.tfm) = %{tl_version}, tex(lmtlc8ttl10.tfm) = %{tl_version}
Provides:       tex(lmtlco8ttl10.tfm) = %{tl_version}, tex(lmtlo8ttl10.tfm) = %{tl_version}
Provides:       tex(lmtt8ttl10.tfm) = %{tl_version}, tex(lmtt8ttl12.tfm) = %{tl_version}
Provides:       tex(lmtt8ttl8.tfm) = %{tl_version}, tex(lmtt8ttl9.tfm) = %{tl_version}
Provides:       tex(lmtti8ttl10.tfm) = %{tl_version}, tex(lmtto8ttl10.tfm) = %{tl_version}
Provides:       tex(lmu8ttl10.tfm) = %{tl_version}, tex(lmvtk8ttl10.tfm) = %{tl_version}
Provides:       tex(lmvtko8ttl10.tfm) = %{tl_version}, tex(lmvtl8ttl10.tfm) = %{tl_version}
Provides:       tex(lmvtlo8ttl10.tfm) = %{tl_version}, tex(lmvtt8ttl10.tfm) = %{tl_version}
Provides:       tex(lmvtto8ttl10.tfm) = %{tl_version}, tex(u-clmb10.tfm) = %{tl_version}
Provides:       tex(u-clmbo10.tfm) = %{tl_version}, tex(u-clmbx10.tfm) = %{tl_version}
Provides:       tex(u-clmbx12.tfm) = %{tl_version}, tex(u-clmbx5.tfm) = %{tl_version}
Provides:       tex(u-clmbx6.tfm) = %{tl_version}, tex(u-clmbx7.tfm) = %{tl_version}
Provides:       tex(u-clmbx8.tfm) = %{tl_version}, tex(u-clmbx9.tfm) = %{tl_version}
Provides:       tex(u-clmbxi10.tfm) = %{tl_version}, tex(u-clmbxo10.tfm) = %{tl_version}
Provides:       tex(u-clmcsc10.tfm) = %{tl_version}, tex(u-clmcsco10.tfm) = %{tl_version}
Provides:       tex(u-clmdunh10.tfm) = %{tl_version}, tex(u-clmduno10.tfm) = %{tl_version}
Provides:       tex(u-clmr10.tfm) = %{tl_version}, tex(u-clmr12.tfm) = %{tl_version}
Provides:       tex(u-clmr17.tfm) = %{tl_version}, tex(u-clmr5.tfm) = %{tl_version}
Provides:       tex(u-clmr6.tfm) = %{tl_version}, tex(u-clmr7.tfm) = %{tl_version}
Provides:       tex(u-clmr8.tfm) = %{tl_version}, tex(u-clmr9.tfm) = %{tl_version}
Provides:       tex(u-clmri10.tfm) = %{tl_version}, tex(u-clmri12.tfm) = %{tl_version}
Provides:       tex(u-clmri7.tfm) = %{tl_version}, tex(u-clmri8.tfm) = %{tl_version}
Provides:       tex(u-clmri9.tfm) = %{tl_version}, tex(u-clmro10.tfm) = %{tl_version}
Provides:       tex(u-clmro12.tfm) = %{tl_version}, tex(u-clmro17.tfm) = %{tl_version}
Provides:       tex(u-clmro8.tfm) = %{tl_version}, tex(u-clmro9.tfm) = %{tl_version}
Provides:       tex(u-clmss10.tfm) = %{tl_version}, tex(u-clmss12.tfm) = %{tl_version}
Provides:       tex(u-clmss17.tfm) = %{tl_version}, tex(u-clmss8.tfm) = %{tl_version}
Provides:       tex(u-clmss9.tfm) = %{tl_version}, tex(u-clmssbo10.tfm) = %{tl_version}
Provides:       tex(u-clmssbx10.tfm) = %{tl_version}, tex(u-clmssdc10.tfm) = %{tl_version}
Provides:       tex(u-clmssdo10.tfm) = %{tl_version}, tex(u-clmsso10.tfm) = %{tl_version}
Provides:       tex(u-clmsso12.tfm) = %{tl_version}, tex(u-clmsso17.tfm) = %{tl_version}
Provides:       tex(u-clmsso8.tfm) = %{tl_version}, tex(u-clmsso9.tfm) = %{tl_version}
Provides:       tex(u-clmssq8.tfm) = %{tl_version}, tex(u-clmssqbo8.tfm) = %{tl_version}
Provides:       tex(u-clmssqbx8.tfm) = %{tl_version}, tex(u-clmssqo8.tfm) = %{tl_version}
Provides:       tex(u-clmtcsc10.tfm) = %{tl_version}, tex(u-clmtcso10.tfm) = %{tl_version}
Provides:       tex(u-clmtk10.tfm) = %{tl_version}, tex(u-clmtko10.tfm) = %{tl_version}
Provides:       tex(u-clmtl10.tfm) = %{tl_version}, tex(u-clmtlc10.tfm) = %{tl_version}
Provides:       tex(u-clmtlco10.tfm) = %{tl_version}, tex(u-clmtlo10.tfm) = %{tl_version}
Provides:       tex(u-clmtt10.tfm) = %{tl_version}, tex(u-clmtt12.tfm) = %{tl_version}
Provides:       tex(u-clmtt8.tfm) = %{tl_version}, tex(u-clmtt9.tfm) = %{tl_version}
Provides:       tex(u-clmtti10.tfm) = %{tl_version}, tex(u-clmtto10.tfm) = %{tl_version}
Provides:       tex(u-clmu10.tfm) = %{tl_version}, tex(u-clmvtk10.tfm) = %{tl_version}
Provides:       tex(u-clmvtko10.tfm) = %{tl_version}, tex(u-clmvtl10.tfm) = %{tl_version}
Provides:       tex(u-clmvtlo10.tfm) = %{tl_version}, tex(u-clmvtt10.tfm) = %{tl_version}
Provides:       tex(u-clmvtto10.tfm) = %{tl_version}, tex(clmb28t10.vf) = %{tl_version}
Provides:       tex(clmb2j8t10.vf) = %{tl_version}, tex(clmb2jo8t10.vf) = %{tl_version}
Provides:       tex(clmb2o8t10.vf) = %{tl_version}, tex(clmb8t10.vf) = %{tl_version}
Provides:       tex(clmbj8t10.vf) = %{tl_version}, tex(clmbjo8t10.vf) = %{tl_version}
Provides:       tex(clmbo8t10.vf) = %{tl_version}, tex(clmbx28t10.vf) = %{tl_version}
Provides:       tex(clmbx28t12.vf) = %{tl_version}, tex(clmbx28t5.vf) = %{tl_version}
Provides:       tex(clmbx28t6.vf) = %{tl_version}, tex(clmbx28t7.vf) = %{tl_version}
Provides:       tex(clmbx28t8.vf) = %{tl_version}, tex(clmbx28t9.vf) = %{tl_version}
Provides:       tex(clmbx2i8t10.vf) = %{tl_version}, tex(clmbx2ij8t10.vf) = %{tl_version}
Provides:       tex(clmbx2j8t10.vf) = %{tl_version}, tex(clmbx2j8t12.vf) = %{tl_version}
Provides:       tex(clmbx2j8t5.vf) = %{tl_version}, tex(clmbx2j8t6.vf) = %{tl_version}
Provides:       tex(clmbx2j8t7.vf) = %{tl_version}, tex(clmbx2j8t8.vf) = %{tl_version}
Provides:       tex(clmbx2j8t9.vf) = %{tl_version}, tex(clmbx2jo8t10.vf) = %{tl_version}
Provides:       tex(clmbx2o8t10.vf) = %{tl_version}, tex(clmbx8t10.vf) = %{tl_version}
Provides:       tex(clmbx8t12.vf) = %{tl_version}, tex(clmbx8t5.vf) = %{tl_version}
Provides:       tex(clmbx8t6.vf) = %{tl_version}, tex(clmbx8t7.vf) = %{tl_version}
Provides:       tex(clmbx8t8.vf) = %{tl_version}, tex(clmbx8t9.vf) = %{tl_version}
Provides:       tex(clmbxi8t10.vf) = %{tl_version}, tex(clmbxj8t10.vf) = %{tl_version}
Provides:       tex(clmbxj8t12.vf) = %{tl_version}, tex(clmbxj8t5.vf) = %{tl_version}
Provides:       tex(clmbxj8t6.vf) = %{tl_version}, tex(clmbxj8t7.vf) = %{tl_version}
Provides:       tex(clmbxj8t8.vf) = %{tl_version}, tex(clmbxj8t9.vf) = %{tl_version}
Provides:       tex(clmbxji8t10.vf) = %{tl_version}, tex(clmbxjo8t10.vf) = %{tl_version}
Provides:       tex(clmbxo8t10.vf) = %{tl_version}, tex(clmcsc28t10.vf) = %{tl_version}
Provides:       tex(clmcsc2j8t10.vf) = %{tl_version}, tex(clmcsc2jo8t10.vf) = %{tl_version}
Provides:       tex(clmcsc2o8t10.vf) = %{tl_version}, tex(clmcsc8t10.vf) = %{tl_version}
Provides:       tex(clmcscj8t10.vf) = %{tl_version}, tex(clmcscjo8t10.vf) = %{tl_version}
Provides:       tex(clmcsco8t10.vf) = %{tl_version}, tex(clmdun2jo8t10.vf) = %{tl_version}
Provides:       tex(clmdun2o8t10.vf) = %{tl_version}, tex(clmdunh28t10.vf) = %{tl_version}
Provides:       tex(clmdunh2j8t10.vf) = %{tl_version}, tex(clmdunh8t10.vf) = %{tl_version}
Provides:       tex(clmdunhj8t10.vf) = %{tl_version}, tex(clmdunjo8t10.vf) = %{tl_version}
Provides:       tex(clmduno8t10.vf) = %{tl_version}, tex(clmr28t10.vf) = %{tl_version}
Provides:       tex(clmr28t12.vf) = %{tl_version}, tex(clmr28t17.vf) = %{tl_version}
Provides:       tex(clmr28t5.vf) = %{tl_version}, tex(clmr28t6.vf) = %{tl_version}
Provides:       tex(clmr28t7.vf) = %{tl_version}, tex(clmr28t8.vf) = %{tl_version}
Provides:       tex(clmr28t9.vf) = %{tl_version}, tex(clmr2i8t10.vf) = %{tl_version}
Provides:       tex(clmr2i8t12.vf) = %{tl_version}, tex(clmr2i8t7.vf) = %{tl_version}
Provides:       tex(clmr2i8t8.vf) = %{tl_version}, tex(clmr2i8t9.vf) = %{tl_version}
Provides:       tex(clmr2ij8t10.vf) = %{tl_version}, tex(clmr2ij8t12.vf) = %{tl_version}
Provides:       tex(clmr2ij8t7.vf) = %{tl_version}, tex(clmr2ij8t8.vf) = %{tl_version}
Provides:       tex(clmr2ij8t9.vf) = %{tl_version}, tex(clmr2j8t10.vf) = %{tl_version}
Provides:       tex(clmr2j8t12.vf) = %{tl_version}, tex(clmr2j8t17.vf) = %{tl_version}
Provides:       tex(clmr2j8t5.vf) = %{tl_version}, tex(clmr2j8t6.vf) = %{tl_version}
Provides:       tex(clmr2j8t7.vf) = %{tl_version}, tex(clmr2j8t8.vf) = %{tl_version}
Provides:       tex(clmr2j8t9.vf) = %{tl_version}, tex(clmr2jo8t10.vf) = %{tl_version}
Provides:       tex(clmr2jo8t12.vf) = %{tl_version}, tex(clmr2jo8t17.vf) = %{tl_version}
Provides:       tex(clmr2jo8t8.vf) = %{tl_version}, tex(clmr2jo8t9.vf) = %{tl_version}
Provides:       tex(clmr2o8t10.vf) = %{tl_version}, tex(clmr2o8t12.vf) = %{tl_version}
Provides:       tex(clmr2o8t17.vf) = %{tl_version}, tex(clmr2o8t8.vf) = %{tl_version}
Provides:       tex(clmr2o8t9.vf) = %{tl_version}, tex(clmr8t10.vf) = %{tl_version}
Provides:       tex(clmr8t12.vf) = %{tl_version}, tex(clmr8t17.vf) = %{tl_version}
Provides:       tex(clmr8t5.vf) = %{tl_version}, tex(clmr8t6.vf) = %{tl_version}
Provides:       tex(clmr8t7.vf) = %{tl_version}, tex(clmr8t8.vf) = %{tl_version}
Provides:       tex(clmr8t9.vf) = %{tl_version}, tex(clmri8t10.vf) = %{tl_version}
Provides:       tex(clmri8t12.vf) = %{tl_version}, tex(clmri8t7.vf) = %{tl_version}
Provides:       tex(clmri8t8.vf) = %{tl_version}, tex(clmri8t9.vf) = %{tl_version}
Provides:       tex(clmrj8t10.vf) = %{tl_version}, tex(clmrj8t12.vf) = %{tl_version}
Provides:       tex(clmrj8t17.vf) = %{tl_version}, tex(clmrj8t5.vf) = %{tl_version}
Provides:       tex(clmrj8t6.vf) = %{tl_version}, tex(clmrj8t7.vf) = %{tl_version}
Provides:       tex(clmrj8t8.vf) = %{tl_version}, tex(clmrj8t9.vf) = %{tl_version}
Provides:       tex(clmrji8t10.vf) = %{tl_version}, tex(clmrji8t12.vf) = %{tl_version}
Provides:       tex(clmrji8t7.vf) = %{tl_version}, tex(clmrji8t8.vf) = %{tl_version}
Provides:       tex(clmrji8t9.vf) = %{tl_version}, tex(clmrjo8t10.vf) = %{tl_version}
Provides:       tex(clmrjo8t12.vf) = %{tl_version}, tex(clmrjo8t17.vf) = %{tl_version}
Provides:       tex(clmrjo8t8.vf) = %{tl_version}, tex(clmrjo8t9.vf) = %{tl_version}
Provides:       tex(clmro8t10.vf) = %{tl_version}, tex(clmro8t12.vf) = %{tl_version}
Provides:       tex(clmro8t17.vf) = %{tl_version}, tex(clmro8t8.vf) = %{tl_version}
Provides:       tex(clmro8t9.vf) = %{tl_version}, tex(clmss28t10.vf) = %{tl_version}
Provides:       tex(clmss28t12.vf) = %{tl_version}, tex(clmss28t17.vf) = %{tl_version}
Provides:       tex(clmss28t8.vf) = %{tl_version}, tex(clmss28t9.vf) = %{tl_version}
Provides:       tex(clmss2j8t10.vf) = %{tl_version}, tex(clmss2j8t12.vf) = %{tl_version}
Provides:       tex(clmss2j8t17.vf) = %{tl_version}, tex(clmss2j8t8.vf) = %{tl_version}
Provides:       tex(clmss2j8t9.vf) = %{tl_version}, tex(clmss2jo8t10.vf) = %{tl_version}
Provides:       tex(clmss2jo8t12.vf) = %{tl_version}, tex(clmss2jo8t17.vf) = %{tl_version}
Provides:       tex(clmss2jo8t8.vf) = %{tl_version}, tex(clmss2jo8t9.vf) = %{tl_version}
Provides:       tex(clmss8t10.vf) = %{tl_version}, tex(clmss8t12.vf) = %{tl_version}
Provides:       tex(clmss8t17.vf) = %{tl_version}, tex(clmss8t8.vf) = %{tl_version}
Provides:       tex(clmss8t9.vf) = %{tl_version}, tex(clmssb2jo8t10.vf) = %{tl_version}
Provides:       tex(clmssb2o8t10.vf) = %{tl_version}, tex(clmssbjo8t10.vf) = %{tl_version}
Provides:       tex(clmssbo8t10.vf) = %{tl_version}, tex(clmssbx28t10.vf) = %{tl_version}
Provides:       tex(clmssbx2j8t10.vf) = %{tl_version}, tex(clmssbx8t10.vf) = %{tl_version}
Provides:       tex(clmssbxj8t10.vf) = %{tl_version}, tex(clmssd2jo8t10.vf) = %{tl_version}
Provides:       tex(clmssd2o8t10.vf) = %{tl_version}, tex(clmssdc28t10.vf) = %{tl_version}
Provides:       tex(clmssdc2j8t10.vf) = %{tl_version}, tex(clmssdc8t10.vf) = %{tl_version}
Provides:       tex(clmssdcj8t10.vf) = %{tl_version}, tex(clmssdjo8t10.vf) = %{tl_version}
Provides:       tex(clmssdo8t10.vf) = %{tl_version}, tex(clmssj8t10.vf) = %{tl_version}
Provides:       tex(clmssj8t12.vf) = %{tl_version}, tex(clmssj8t17.vf) = %{tl_version}
Provides:       tex(clmssj8t8.vf) = %{tl_version}, tex(clmssj8t9.vf) = %{tl_version}
Provides:       tex(clmssjo8t10.vf) = %{tl_version}, tex(clmssjo8t12.vf) = %{tl_version}
Provides:       tex(clmssjo8t17.vf) = %{tl_version}, tex(clmssjo8t8.vf) = %{tl_version}
Provides:       tex(clmssjo8t9.vf) = %{tl_version}, tex(clmsso28t10.vf) = %{tl_version}
Provides:       tex(clmsso28t12.vf) = %{tl_version}, tex(clmsso28t17.vf) = %{tl_version}
Provides:       tex(clmsso28t8.vf) = %{tl_version}, tex(clmsso28t9.vf) = %{tl_version}
Provides:       tex(clmsso8t10.vf) = %{tl_version}, tex(clmsso8t12.vf) = %{tl_version}
Provides:       tex(clmsso8t17.vf) = %{tl_version}, tex(clmsso8t8.vf) = %{tl_version}
Provides:       tex(clmsso8t9.vf) = %{tl_version}, tex(clmssq28t8.vf) = %{tl_version}
Provides:       tex(clmssq2j8t8.vf) = %{tl_version}, tex(clmssq2jo8t8.vf) = %{tl_version}
Provides:       tex(clmssq2o8t8.vf) = %{tl_version}, tex(clmssq8t8.vf) = %{tl_version}
Provides:       tex(clmssqb2jo8t8.vf) = %{tl_version}, tex(clmssqb2o8t8.vf) = %{tl_version}
Provides:       tex(clmssqbjo8t8.vf) = %{tl_version}, tex(clmssqbo8t8.vf) = %{tl_version}
Provides:       tex(clmssqbx28t8.vf) = %{tl_version}, tex(clmssqbx2j8t8.vf) = %{tl_version}
Provides:       tex(clmssqbx8t8.vf) = %{tl_version}, tex(clmssqbxj8t8.vf) = %{tl_version}
Provides:       tex(clmssqj8t8.vf) = %{tl_version}, tex(clmssqjo8t8.vf) = %{tl_version}
Provides:       tex(clmssqo8t8.vf) = %{tl_version}, tex(clmtcsc8t10.vf) = %{tl_version}
Provides:       tex(clmtcscj8t10.vf) = %{tl_version}, tex(clmtcsjo8t10.vf) = %{tl_version}
Provides:       tex(clmtcso8t10.vf) = %{tl_version}, tex(clmtk8t10.vf) = %{tl_version}
Provides:       tex(clmtkj8t10.vf) = %{tl_version}, tex(clmtkjo8t10.vf) = %{tl_version}
Provides:       tex(clmtko8t10.vf) = %{tl_version}, tex(clmtl8t10.vf) = %{tl_version}
Provides:       tex(clmtlc8t10.vf) = %{tl_version}, tex(clmtlcj8t10.vf) = %{tl_version}
Provides:       tex(clmtlcjo8t10.vf) = %{tl_version}, tex(clmtlco8t10.vf) = %{tl_version}
Provides:       tex(clmtlj8t10.vf) = %{tl_version}, tex(clmtljo8t10.vf) = %{tl_version}
Provides:       tex(clmtlo8t10.vf) = %{tl_version}, tex(clmtt8t10.vf) = %{tl_version}
Provides:       tex(clmtt8t12.vf) = %{tl_version}, tex(clmtt8t8.vf) = %{tl_version}
Provides:       tex(clmtt8t9.vf) = %{tl_version}, tex(clmtti8t10.vf) = %{tl_version}
Provides:       tex(clmttij8t10.vf) = %{tl_version}, tex(clmttj8t10.vf) = %{tl_version}
Provides:       tex(clmttj8t12.vf) = %{tl_version}, tex(clmttj8t8.vf) = %{tl_version}
Provides:       tex(clmttj8t9.vf) = %{tl_version}, tex(clmttjo8t10.vf) = %{tl_version}
Provides:       tex(clmtto8t10.vf) = %{tl_version}, tex(clmu28t10.vf) = %{tl_version}
Provides:       tex(clmu2j8t10.vf) = %{tl_version}, tex(clmu8t10.vf) = %{tl_version}
Provides:       tex(clmuj8t10.vf) = %{tl_version}, tex(clmvtk28t10.vf) = %{tl_version}
Provides:       tex(clmvtk2j8t10.vf) = %{tl_version}, tex(clmvtk2jo8t10.vf) = %{tl_version}
Provides:       tex(clmvtk2o8t10.vf) = %{tl_version}, tex(clmvtk8t10.vf) = %{tl_version}
Provides:       tex(clmvtkj8t10.vf) = %{tl_version}, tex(clmvtkjo8t10.vf) = %{tl_version}
Provides:       tex(clmvtko8t10.vf) = %{tl_version}, tex(clmvtl28t10.vf) = %{tl_version}
Provides:       tex(clmvtl2j8t10.vf) = %{tl_version}, tex(clmvtl2jo8t10.vf) = %{tl_version}
Provides:       tex(clmvtl2o8t10.vf) = %{tl_version}, tex(clmvtl8t10.vf) = %{tl_version}
Provides:       tex(clmvtlj8t10.vf) = %{tl_version}, tex(clmvtljo8t10.vf) = %{tl_version}
Provides:       tex(clmvtlo8t10.vf) = %{tl_version}, tex(clmvtt28t10.vf) = %{tl_version}
Provides:       tex(clmvtt2j8t10.vf) = %{tl_version}, tex(clmvtt2jo8t10.vf) = %{tl_version}
Provides:       tex(clmvtt2o8t10.vf) = %{tl_version}, tex(clmvtt8t10.vf) = %{tl_version}
Provides:       tex(clmvttj8t10.vf) = %{tl_version}, tex(clmvttjo8t10.vf) = %{tl_version}
Provides:       tex(clmvtto8t10.vf) = %{tl_version}, tex(u-clmb10.vf) = %{tl_version}
Provides:       tex(u-clmbo10.vf) = %{tl_version}, tex(u-clmbx10.vf) = %{tl_version}
Provides:       tex(u-clmbx12.vf) = %{tl_version}, tex(u-clmbx5.vf) = %{tl_version}
Provides:       tex(u-clmbx6.vf) = %{tl_version}, tex(u-clmbx7.vf) = %{tl_version}
Provides:       tex(u-clmbx8.vf) = %{tl_version}, tex(u-clmbx9.vf) = %{tl_version}
Provides:       tex(u-clmbxi10.vf) = %{tl_version}, tex(u-clmbxo10.vf) = %{tl_version}
Provides:       tex(u-clmcsc10.vf) = %{tl_version}, tex(u-clmcsco10.vf) = %{tl_version}
Provides:       tex(u-clmdunh10.vf) = %{tl_version}, tex(u-clmduno10.vf) = %{tl_version}
Provides:       tex(u-clmr10.vf) = %{tl_version}, tex(u-clmr12.vf) = %{tl_version}
Provides:       tex(u-clmr17.vf) = %{tl_version}, tex(u-clmr5.vf) = %{tl_version}
Provides:       tex(u-clmr6.vf) = %{tl_version}, tex(u-clmr7.vf) = %{tl_version}
Provides:       tex(u-clmr8.vf) = %{tl_version}, tex(u-clmr9.vf) = %{tl_version}
Provides:       tex(u-clmri10.vf) = %{tl_version}, tex(u-clmri12.vf) = %{tl_version}
Provides:       tex(u-clmri7.vf) = %{tl_version}, tex(u-clmri8.vf) = %{tl_version}
Provides:       tex(u-clmri9.vf) = %{tl_version}, tex(u-clmro10.vf) = %{tl_version}
Provides:       tex(u-clmro12.vf) = %{tl_version}, tex(u-clmro17.vf) = %{tl_version}
Provides:       tex(u-clmro8.vf) = %{tl_version}, tex(u-clmro9.vf) = %{tl_version}
Provides:       tex(u-clmss10.vf) = %{tl_version}, tex(u-clmss12.vf) = %{tl_version}
Provides:       tex(u-clmss17.vf) = %{tl_version}, tex(u-clmss8.vf) = %{tl_version}
Provides:       tex(u-clmss9.vf) = %{tl_version}, tex(u-clmssbo10.vf) = %{tl_version}
Provides:       tex(u-clmssbx10.vf) = %{tl_version}, tex(u-clmssdc10.vf) = %{tl_version}
Provides:       tex(u-clmssdo10.vf) = %{tl_version}, tex(u-clmsso10.vf) = %{tl_version}
Provides:       tex(u-clmsso12.vf) = %{tl_version}, tex(u-clmsso17.vf) = %{tl_version}
Provides:       tex(u-clmsso8.vf) = %{tl_version}, tex(u-clmsso9.vf) = %{tl_version}
Provides:       tex(u-clmssq8.vf) = %{tl_version}, tex(u-clmssqbo8.vf) = %{tl_version}
Provides:       tex(u-clmssqbx8.vf) = %{tl_version}, tex(u-clmssqo8.vf) = %{tl_version}
Provides:       tex(u-clmtcsc10.vf) = %{tl_version}, tex(u-clmtcso10.vf) = %{tl_version}
Provides:       tex(u-clmtk10.vf) = %{tl_version}, tex(u-clmtko10.vf) = %{tl_version}
Provides:       tex(u-clmtl10.vf) = %{tl_version}, tex(u-clmtlc10.vf) = %{tl_version}
Provides:       tex(u-clmtlco10.vf) = %{tl_version}, tex(u-clmtlo10.vf) = %{tl_version}
Provides:       tex(u-clmtt10.vf) = %{tl_version}, tex(u-clmtt12.vf) = %{tl_version}
Provides:       tex(u-clmtt8.vf) = %{tl_version}, tex(u-clmtt9.vf) = %{tl_version}
Provides:       tex(u-clmtti10.vf) = %{tl_version}, tex(u-clmtto10.vf) = %{tl_version}
Provides:       tex(u-clmu10.vf) = %{tl_version}, tex(u-clmvtk10.vf) = %{tl_version}
Provides:       tex(u-clmvtko10.vf) = %{tl_version}, tex(u-clmvtl10.vf) = %{tl_version}
Provides:       tex(u-clmvtlo10.vf) = %{tl_version}, tex(u-clmvtt10.vf) = %{tl_version}
Provides:       tex(u-clmvtto10.vf) = %{tl_version}, tex(cfr-lm.sty) = %{tl_version}
Provides:       tex(t1clm.fd) = %{tl_version}, tex(t1clm2.fd) = %{tl_version}
Provides:       tex(t1clm2d.fd) = %{tl_version}, tex(t1clm2dj.fd) = %{tl_version}
Provides:       tex(t1clm2j.fd) = %{tl_version}, tex(t1clm2jqs.fd) = %{tl_version}
Provides:       tex(t1clm2js.fd) = %{tl_version}, tex(t1clm2jt.fd) = %{tl_version}
Provides:       tex(t1clm2jv.fd) = %{tl_version}, tex(t1clm2qs.fd) = %{tl_version}
Provides:       tex(t1clm2s.fd) = %{tl_version}, tex(t1clm2t.fd) = %{tl_version}
Provides:       tex(t1clm2v.fd) = %{tl_version}, tex(t1clmd.fd) = %{tl_version}
Provides:       tex(t1clmdj.fd) = %{tl_version}, tex(t1clmj.fd) = %{tl_version}
Provides:       tex(t1clmjqs.fd) = %{tl_version}, tex(t1clmjs.fd) = %{tl_version}
Provides:       tex(t1clmjt.fd) = %{tl_version}, tex(t1clmjv.fd) = %{tl_version}
Provides:       tex(t1clmqs.fd) = %{tl_version}, tex(t1clms.fd) = %{tl_version}
Provides:       tex(t1clmt.fd) = %{tl_version}, tex(t1clmv.fd) = %{tl_version}
Provides:       tex(ts1clm.fd) = %{tl_version}, tex(ts1clm2.fd) = %{tl_version}
Provides:       tex(ts1clm2d.fd) = %{tl_version}, tex(ts1clm2dj.fd) = %{tl_version}
Provides:       tex(ts1clm2j.fd) = %{tl_version}, tex(ts1clm2jqs.fd) = %{tl_version}
Provides:       tex(ts1clm2js.fd) = %{tl_version}, tex(ts1clm2jt.fd) = %{tl_version}
Provides:       tex(ts1clm2jv.fd) = %{tl_version}, tex(ts1clm2qs.fd) = %{tl_version}
Provides:       tex(ts1clm2s.fd) = %{tl_version}, tex(ts1clm2t.fd) = %{tl_version}
Provides:       tex(ts1clm2v.fd) = %{tl_version}, tex(ts1clmd.fd) = %{tl_version}
Provides:       tex(ts1clmdj.fd) = %{tl_version}, tex(ts1clmj.fd) = %{tl_version}
Provides:       tex(ts1clmjqs.fd) = %{tl_version}, tex(ts1clmjs.fd) = %{tl_version}
Provides:       tex(ts1clmjt.fd) = %{tl_version}, tex(ts1clmjv.fd) = %{tl_version}
Provides:       tex(ts1clmqs.fd) = %{tl_version}, tex(ts1clms.fd) = %{tl_version}
Provides:       tex(ts1clmt.fd) = %{tl_version}, tex(ts1clmv.fd) = %{tl_version}
Provides:       tex(uclm.fd) = %{tl_version}, tex(uclm2.fd) = %{tl_version}
Provides:       tex(uclm2d.fd) = %{tl_version}, tex(uclm2dj.fd) = %{tl_version}
Provides:       tex(uclm2j.fd) = %{tl_version}, tex(uclm2jqs.fd) = %{tl_version}
Provides:       tex(uclm2js.fd) = %{tl_version}, tex(uclm2jt.fd) = %{tl_version}
Provides:       tex(uclm2jv.fd) = %{tl_version}, tex(uclm2qs.fd) = %{tl_version}
Provides:       tex(uclm2s.fd) = %{tl_version}, tex(uclm2t.fd) = %{tl_version}
Provides:       tex(uclm2v.fd) = %{tl_version}, tex(uclmd.fd) = %{tl_version}
Provides:       tex(uclmdj.fd) = %{tl_version}, tex(uclmj.fd) = %{tl_version}
Provides:       tex(uclmjqs.fd) = %{tl_version}, tex(uclmjs.fd) = %{tl_version}
Provides:       tex(uclmjt.fd) = %{tl_version}, tex(uclmjv.fd) = %{tl_version}
Provides:       tex(uclmqs.fd) = %{tl_version}, tex(uclms.fd) = %{tl_version}
Provides:       tex(uclmt.fd) = %{tl_version}, tex(uclmv.fd) = %{tl_version}

%description -n texlive-cfr-lm
The package supports a number of features of the Latin Modern
fonts which are not easily accessible via the default (La)TeX
support provided in the official distribution. In particular,
the package supports the use of the various styles of digits
available, small-caps and upright italic shapes, and
alternative weights and widths. It also supports variable width
typewriter and the "quotation" font. Version 2.004 of the Latin
Modern fonts is supported. By default, the package uses
proportional oldstyle digits and variable width typewriter but
this can be changed by passing appropriate options to the
package. The package also supports using (for example)
different styles of digits within a document so it is possible
to use proportional oldstyle digits by default, say, but
tabular lining digits within a particular table. The package
requires the official Latin Modern distribution, including its
(La)TeX support. The package relies on the availability of both
the fonts themselves and the official font support files. The
package also makes use of the nfssext-cfr package. Only the T1
and TS1 encodings are supported for text fonts. The set up of
fonts for mathematics is identical to that provided by Latin
Modern.

%package -n texlive-cfr-lm-doc
Summary:        Documentation for cfr-lm
Version:        svn36195.1.5

Provides:       tex-cfr-lm-doc
AutoReqProv:    No

%description -n texlive-cfr-lm-doc
Documentation for cfr-lm

%package -n texlive-changebar
Provides:       tex-changebar = %{tl_version}
License:        LPPL
Summary:        Generate changebars in LaTeX documents
Version:        svn46919
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(changebar.sty) = %{tl_version}

%description -n texlive-changebar
Identify areas of text to be marked with changebars with the
\cbstart and \cbend commands; the bars may be coloured. The
package uses 'drivers' to place the bars; the available drivers
can work with dvitoln03, dvitops, dvips, the emTeX and TeXtures
DVI drivers, and VTeX and PDFTeX.

%package -n texlive-changebar-doc
Summary:        Documentation for changebar
Version:        svn46919
Provides:       tex-changebar-doc
AutoReqProv:    No

%description -n texlive-changebar-doc
Documentation for changebar

%package -n texlive-changelayout
Provides:       tex-changelayout = %{tl_version}
License:        LPPL
Summary:        Change the layout of individual pages and their text
Version:        svn16094.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(etextools.sty), tex(xkeyval.sty), tex(ltxnew.sty), tex(xcolor.sty)
Provides:       tex(changelayout.sty) = %{tl_version}

%description -n texlive-changelayout
The package is an extension of the changepage package to permit
the user to change the layout of individual pages and their
texts.

%package -n texlive-changelayout-doc
Summary:        Documentation for changelayout
Version:        svn16094.1.0

Provides:       tex-changelayout-doc
AutoReqProv:    No

%description -n texlive-changelayout-doc
Documentation for changelayout

%package -n texlive-changepage
Provides:       tex-changepage = %{tl_version}
License:        LPPL 1.3
Summary:        Margin adjustment and detection of odd/even pages
Version:        svn15878.1.0c

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(changepage.sty) = %{tl_version}, tex(chngpage.sty) = %{tl_version}

%description -n texlive-changepage
The package provides commands to change the page layout in the
middle of a document, and to robustly check for typesetting on
odd or even pages. Instructions for use are at the end of the
file. The package is an extraction of code from the memoir
class, whose user interface it shares. It is intended the this
package will eventually replace the chngpage package, which is
distributed with the package.

%package -n texlive-changepage-doc
Summary:        Documentation for changepage
Version:        svn15878.1.0c

Provides:       tex-changepage-doc
AutoReqProv:    No

%description -n texlive-changepage-doc
Documentation for changepage

%package -n texlive-changes
Provides:       tex-changes = %{tl_version}
License:        LPPL 1.3
Summary:        Manual change markup
Version:        svn41737
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(xifthen.sty), tex(xcolor.sty), tex(pdfcolmk.sty)
Requires:       tex(ulem.sty), tex(truncate.sty)
Provides:       tex(changes.sty) = %{tl_version}

%description -n texlive-changes
The package allows the user to manually markup changes of text,
such as additions, deletions, or replacements. Changed text is
shown in a different colour; deleted text is crossed out. The
package allows definition of additional authors and their
associated colour. It also allows you to define a markup for
authors or annotations. A bash script is provided for removing
the changes.

%package -n texlive-changes-doc
Summary:        Documentation for changes
Version:        svn41737
Provides:       tex-changes-doc
AutoReqProv:    No

%description -n texlive-changes-doc
Documentation for changes

%package -n texlive-chappg
Provides:       tex-chappg = %{tl_version}
License:        LPPL
Summary:        Page numbering by chapter
Version:        svn15878.2.1b

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chappg.sty) = %{tl_version}

%description -n texlive-chappg
The package provides for 'chapterno-pageno' or 'chaptername-
pageno' page numbering. Provision is made for front- and
backmatter in book class.

%package -n texlive-chappg-doc
Summary:        Documentation for chappg
Version:        svn15878.2.1b

Provides:       tex-chappg-doc
AutoReqProv:    No

%description -n texlive-chappg-doc
Documentation for chappg

%package -n texlive-chapterfolder
Provides:       tex-chapterfolder = %{tl_version}
License:        LPPL
Summary:        Package for working with complicated folder structures
Version:        svn15878.2.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty)
Provides:       tex(chapterfolder.sty) = %{tl_version}

%description -n texlive-chapterfolder
This package simplifies working with folder structures that
match the chapter/section/subsection structure. It provides
macros to define a folder that contains the file for a
chapter/section/subsection, and provides macros that allow
inclusion without using the full path, rather the path relative
to the current folder of the chapter/section/subsection. It
makes easy changing the name of a folder, for example.

%package -n texlive-chapterfolder-doc
Summary:        Documentation for chapterfolder
Version:        svn15878.2.0.1

Provides:       tex-chapterfolder-doc
AutoReqProv:    No

%description -n texlive-chapterfolder-doc
Documentation for chapterfolder

%package -n texlive-charter
Provides:       tex-charter = %{tl_version}
License:        Copyright only
Summary:        Charter fonts
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bchb7t.tfm) = %{tl_version}, tex(bchb8c.tfm) = %{tl_version}
Provides:       tex(bchb8r.tfm) = %{tl_version}, tex(bchb8t.tfm) = %{tl_version}
Provides:       tex(bchbc7t.tfm) = %{tl_version}, tex(bchbc8t.tfm) = %{tl_version}
Provides:       tex(bchbi7t.tfm) = %{tl_version}, tex(bchbi8c.tfm) = %{tl_version}
Provides:       tex(bchbi8r.tfm) = %{tl_version}, tex(bchbi8t.tfm) = %{tl_version}
Provides:       tex(bchbo7t.tfm) = %{tl_version}, tex(bchbo8c.tfm) = %{tl_version}
Provides:       tex(bchbo8r.tfm) = %{tl_version}, tex(bchbo8t.tfm) = %{tl_version}
Provides:       tex(bchr7t.tfm) = %{tl_version}, tex(bchr8c.tfm) = %{tl_version}
Provides:       tex(bchr8r.tfm) = %{tl_version}, tex(bchr8t.tfm) = %{tl_version}
Provides:       tex(bchrc7t.tfm) = %{tl_version}, tex(bchrc8t.tfm) = %{tl_version}
Provides:       tex(bchri7t.tfm) = %{tl_version}, tex(bchri8c.tfm) = %{tl_version}
Provides:       tex(bchri8r.tfm) = %{tl_version}, tex(bchri8t.tfm) = %{tl_version}
Provides:       tex(bchro7t.tfm) = %{tl_version}, tex(bchro8c.tfm) = %{tl_version}
Provides:       tex(bchro8r.tfm) = %{tl_version}, tex(bchro8t.tfm) = %{tl_version}
Provides:       tex(bchb8a.pfb) = %{tl_version}, tex(bchbi8a.pfb) = %{tl_version}
Provides:       tex(bchr8a.pfb) = %{tl_version}, tex(bchri8a.pfb) = %{tl_version}
Provides:       tex(bchb7t.vf) = %{tl_version}, tex(bchb8c.vf) = %{tl_version}
Provides:       tex(bchb8t.vf) = %{tl_version}, tex(bchbc7t.vf) = %{tl_version}
Provides:       tex(bchbc8t.vf) = %{tl_version}, tex(bchbi7t.vf) = %{tl_version}
Provides:       tex(bchbi8c.vf) = %{tl_version}, tex(bchbi8t.vf) = %{tl_version}
Provides:       tex(bchbo7t.vf) = %{tl_version}, tex(bchbo8c.vf) = %{tl_version}
Provides:       tex(bchbo8t.vf) = %{tl_version}, tex(bchr7t.vf) = %{tl_version}
Provides:       tex(bchr8c.vf) = %{tl_version}, tex(bchr8t.vf) = %{tl_version}
Provides:       tex(bchrc7t.vf) = %{tl_version}, tex(bchrc8t.vf) = %{tl_version}
Provides:       tex(bchri7t.vf) = %{tl_version}, tex(bchri8c.vf) = %{tl_version}
Provides:       tex(bchri8t.vf) = %{tl_version}, tex(bchro7t.vf) = %{tl_version}
Provides:       tex(bchro8c.vf) = %{tl_version}, tex(bchro8t.vf) = %{tl_version}

%description -n texlive-charter
A commercial text font donated for the common good. Support for
use with LaTeX is available in freenfss, part of psnfss.

%package -n texlive-charter-doc
Summary:        Documentation for charter
Version:        svn15878.0

Provides:       tex-charter-doc
AutoReqProv:    No

%description -n texlive-charter-doc
Documentation for charter

%package -n texlive-chbibref
Provides:       tex-chbibref = %{tl_version}
License:        LPPL
Summary:        Change the Bibliography/References title
Version:        svn17120.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chbibref.sty) = %{tl_version}

%description -n texlive-chbibref
Defines a single command, \setbibref, which sets whichever of
\bibname and \refname is in use. (\bibname is used in book.cls
and report.cls, and \refname is used in article.cls.)

%package -n texlive-chbibref-doc
Summary:        Documentation for chbibref
Version:        svn17120.1.0

Provides:       tex-chbibref-doc
AutoReqProv:    No

%description -n texlive-chbibref-doc
Documentation for chbibref

%package -n texlive-chemarrow
Provides:       tex-chemarrow = %{tl_version}
License:        Public Domain
Summary:        Arrows for use in chemistry
Version:        svn17146.0.9

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Provides:       tex(chemarrow.map) = %{tl_version}, tex(arrow.tfm) = %{tl_version}
Provides:       tex(arrow.pfb) = %{tl_version}, tex(chemarrow.sty) = %{tl_version}

%description -n texlive-chemarrow
This bundle consists of a font (available as Metafont source,
Metapost source, and generated type 1 versions), and a package
to use it. The arrows in the font are designed to look more
like those in chemistry text-books than do Knuth's originals.

%package -n texlive-chemarrow-doc
Summary:        Documentation for chemarrow
Version:        svn17146.0.9

Provides:       tex-chemarrow-doc
AutoReqProv:    No

%description -n texlive-chemarrow-doc
Documentation for chemarrow

%package -n texlive-chembst
Provides:       tex-chembst = %{tl_version}
License:        LPPL
Summary:        A collection of BibTeX files for chemistry journals
Version:        svn15878.0.2.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-chembst
The package offers a collection of advanced BibTeX style files
suitable for publications in chemistry journals. Currently,
style files for journals published by the American Chemical
Society, Wiley-VCH and The Royal Society of Chemistry are
available. The style files support advanced features such as
automatic formatting of errata or creating an appropriate entry
for publications in Angewandte Chemie where both English and
German should be cited simultaneously.

%package -n texlive-chembst-doc
Summary:        Documentation for chembst
Version:        svn15878.0.2.5

Provides:       tex-chembst-doc
AutoReqProv:    No

%description -n texlive-chembst-doc
Documentation for chembst

%package -n texlive-chemcompounds
Provides:       tex-chemcompounds = %{tl_version}
License:        LPPL
Summary:        Simple consecutive numbering of chemical compounds
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chemcompounds.sty) = %{tl_version}

%description -n texlive-chemcompounds
The chemcompounds package allows for a simple consecutive
numbering of chemical compounds. Optionally, it is possible to
supply a custom name for each compound. The package differs
from the chemcono package by not generating an odd-looking list
of compounds inside the text.

%package -n texlive-chemcompounds-doc
Summary:        Documentation for chemcompounds
Version:        svn15878.0

Provides:       tex-chemcompounds-doc
AutoReqProv:    No

%description -n texlive-chemcompounds-doc
Documentation for chemcompounds

%package -n texlive-chemcono
Provides:       tex-chemcono = %{tl_version}
License:        LPPL
Summary:        Support for compound numbers in chemistry documents
Version:        svn17119.1.3

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(color.sty)
Provides:       tex(chemcono.sty) = %{tl_version}, tex(drftcono.sty) = %{tl_version}
Provides:       tex(showkeysff.sty) = %{tl_version}

%description -n texlive-chemcono
A LaTeX package for using compound numbers in chemistry
documents. It works like \cite and the \thebibliography, using
\fcite and \theffbibliography instead. It allows compound names
in documents to be numbered and does not affect the normal
citation routines.

%package -n texlive-chemcono-doc
Summary:        Documentation for chemcono
Version:        svn17119.1.3

Provides:       tex-chemcono-doc
AutoReqProv:    No

%description -n texlive-chemcono-doc
Documentation for chemcono

%package -n texlive-chemexec
Provides:       tex-chemexec = %{tl_version}
License:        LPPL 1.3
Summary:        Creating (chemical) exercise sheets
Version:        svn21632.1.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(amsmath.sty), tex(ifthen.sty), tex(accents.sty)
Requires:       tex(framed.sty), tex(xcolor.sty), tex(xkeyval.sty), tex(tikz.sty)
Requires:       tex(ulem.sty), tex(mhchem.sty)
Provides:       tex(chemexec.sty) = %{tl_version}

%description -n texlive-chemexec
The package provides environments and commands that the author
needed when preparing exercise sheets and other teaching
material. In particular, the package supports the creation of
exercise sheets, with separating printing of solutions

%package -n texlive-chemexec-doc
Summary:        Documentation for chemexec
Version:        svn21632.1.0

Provides:       tex-chemexec-doc
AutoReqProv:    No

%description -n texlive-chemexec-doc
Documentation for chemexec

%package -n texlive-chemfig
Provides:       tex-chemfig = %{tl_version}
License:        LPPL 1.3
Summary:        Draw molecules with easy syntax
Version:        svn47329
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty)
Provides:       tex(chemfig.sty) = %{tl_version}, tex(chemfig.tex) = %{tl_version}
Provides:       tex(t-chemfig.tex) = %{tl_version}

%description -n texlive-chemfig
The package provides the command \chemfig{<code>}, which draws
molecules using the tikz package. The <code> argument provides
instructions for the drawing operation. While the diagrams
produced are essentially 2-dimensional, the package supports
many of the conventional notations for illustrating the 3-
dimensional layout of a molecule. The package uses TikZ for its
actual drawing operations.

%package -n texlive-chemfig-doc
Summary:        Documentation for chemfig
Version:        svn47329
Provides:       tex-chemfig-doc
AutoReqProv:    No

%description -n texlive-chemfig-doc
Documentation for chemfig

%package -n texlive-chemformula
Provides:       tex-chemformula = %{tl_version}
License:        LPPL 1.3
Summary:        Command for typesetting chemical formulas and reactions
Version:        svn43583
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(tikz.sty)
Requires:       tex(amstext.sty), tex(xfrac.sty), tex(nicefrac.sty), tex(scrlfile.sty)
Provides:       tex(chemformula.sty) = %{tl_version}

%description -n texlive-chemformula
The package provides a command to typeset chemical formulas and
reactions in support of other chemistry packages (such as
chemmacros). The package used to be distributed as a part of
chemmacros.

%package -n texlive-chemformula-doc
Summary:        Documentation for chemformula
Version:        svn43583
Provides:       tex-chemformula-doc
AutoReqProv:    No

%description -n texlive-chemformula-doc
Documentation for chemformula

%package -n texlive-chemgreek
Provides:       tex-chemgreek = %{tl_version}
License:        LPPL 1.3
Summary:        Upright Greek letters in chemistry
Version:        svn42758
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(chemgreek.sty) = %{tl_version}

%description -n texlive-chemgreek
The package provides upright Greek letters in support of other
chemistry packages (such as chemmacros). The package used to be
distributed as a part of chemmacros.

%package -n texlive-chemgreek-doc
Summary:        Documentation for chemgreek
Version:        svn42758
Provides:       tex-chemgreek-doc
AutoReqProv:    No

%description -n texlive-chemgreek-doc
Documentation for chemgreek

%package -n texlive-chem-journal
Provides:       tex-chem-journal = %{tl_version}
License:        GPL+
Summary:        Various BibTeX formats for journals in Chemistry
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-chem-journal
Various BibTeX formats for journals in Chemistry, including
Reviews in Computational Chemistry, Journal of Physical
Chemistry, Journal of Computational Chemistry, and Physical
Chemistry Chemical Physics.

%package -n texlive-chemmacros
Provides:       tex-chemmacros = %{tl_version}
License:        LPPL 1.3
Summary:        A collection of macros to support typesetting chemistry documents
Version:        svn45164
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(chemmacros5.sty)
Requires:       tex(environ.sty), tex(scrlfile.sty), tex(etoolbox.sty), tex(translations.sty)
Requires:       tex(xfrac.sty), tex(siunitx.sty), tex(tikz.sty), tex(mathtools.sty)
Requires:       tex(bm.sty), tex(chemformula.sty), tex(chemgreek.sty), tex(ghsystem.sty)
Requires:       tex(xspace.sty)
Provides:       tex(chemmacros.module.acid-base.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.all.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.base.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.charges.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.chemformula.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.greek.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.isotopes.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.lang.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.mechanisms.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.newman.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.nomenclature.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.orbital.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.particles.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.phases.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.reactions.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.redox.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.scheme.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.spectroscopy.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.symbols.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.thermodynamics.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.tikz.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.units.code.tex) = %{tl_version}
Provides:       tex(chemmacros.module.xfrac.code.tex) = %{tl_version}
Provides:       tex(chemmacros.sty) = %{tl_version}, tex(chemmacros4.sty) = %{tl_version}
Provides:       tex(chemmacros5.sty) = %{tl_version}

%description -n texlive-chemmacros
The bundle offers a collection of macros and commands which are
intended to make typesetting chemistry documents faster and
more convenient. Coverage includes some nomenclature commands,
oxidation numbers, thermodynamic data, newman projections, etc.
The package relies on the following supporting packages:
chemformula, providing a command for typesetting chemical
formulae and reactions (doing a similar task to that of
mhchem); chemgreek, offering support for use of greek letters;
and ghsystem, providing for the UN globally harmonised chemical
notation. The packages are written using current versions of
the experimental LaTeX 3 coding conventions and the LaTeX 3
support packages.

%package -n texlive-chemmacros-doc
Summary:        Documentation for chemmacros
Version:        svn45164
Provides:       tex-chemmacros-doc
AutoReqProv:    No

%description -n texlive-chemmacros-doc
Documentation for chemmacros

%package -n texlive-chemnum
Provides:       tex-chemnum = %{tl_version}
License:        LPPL 1.3
Summary:        A method of numbering chemical compounds
Version:        svn40522

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(expl3.sty), tex(xparse.sty), tex(l3keys2e.sty), tex(translations.sty)
Requires:       tex(chemgreek.sty), tex(psfrag.sty)
Provides:       tex(chemnum.sty) = %{tl_version}

%description -n texlive-chemnum
The package defines a \label- and \ref-like commands for
compound numbers. The package requires LaTeX 3 packages expl3
(from the l3kernel bundle) and xparse (from the l3packages
bundle).

%package -n texlive-chemnum-doc
Summary:        Documentation for chemnum
Version:        svn40522

Provides:       tex-chemnum-doc
AutoReqProv:    No

%description -n texlive-chemnum-doc
Documentation for chemnum

%package -n texlive-chemschemex
Provides:       tex-chemschemex = %{tl_version}
License:        LPPL 1.2
Summary:        Typeset and cross-reference chemical schemes based on TikZ code
Version:        svn46723
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(xkeyval.sty), tex(etextools.sty), tex(xargs.sty), tex(ifthen.sty)
Requires:       tex(suffix.sty), tex(fancylabel.sty), tex(graphicx.sty), tex(tikz.sty)
Provides:       tex(chemschemex.sty) = %{tl_version}

%description -n texlive-chemschemex
The package provides a comfortable means of typesetting
chemical schemes, and also offers automatic structure
referencing.

%package -n texlive-chemschemex-doc
Summary:        Documentation for chemschemex
Version:        svn46723
Provides:       tex-chemschemex-doc
AutoReqProv:    No

%description -n texlive-chemschemex-doc
Documentation for chemschemex

%package -n texlive-chemstyle
Provides:       tex-chemstyle = %{tl_version}
License:        LPPL 1.3
Summary:        Writing chemistry with style
Version:        svn31096.2.0m

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty), tex(psfrag.sty), tex(float.sty), tex(floatrow.sty)
Requires:       tex(chemcompounds.sty), tex(bpchem.sty), tex(amstext.sty), tex(caption.sty)
Requires:       tex(siunitx.sty), tex(SIunits.sty), tex(varioref.sty)
Provides:       tex(chemscheme.sty) = %{tl_version}, tex(chemstyle.sty) = %{tl_version}
Provides:       tex(angew.chemstyle.cfg) = %{tl_version}
Provides:       tex(ic.chemstyle.cfg) = %{tl_version}, tex(jacs.chemstyle.cfg) = %{tl_version}
Provides:       tex(jomc.chemstyle.cfg) = %{tl_version}, tex(orglett.chemstyle.cfg) = %{tl_version}
Provides:       tex(rsc.chemstyle.cfg) = %{tl_version}, tex(tetlett.chemstyle.cfg) = %{tl_version}

%description -n texlive-chemstyle
Chemstyle has been developed as a successor to the LaTeX
package provided by the rsc bundle. The package provides an
extensible system for formatting chemistry documents according
to the conventions of a number of leading journals. It also
provides some handy chemistry-related macros. Chemstyle is much
enhanced compared to its predecessor, and users of rsc are
strongly encouraged to migrate (all of the additional macros in
the rsc LaTeX package are present in chemstyle). The package
chemscheme is distributed with chemstyle; chemstyle itself
incorporates ideas that come from the trivfloat package; the
documentation uses the auto-pst-pdf package.

%package -n texlive-chemstyle-doc
Summary:        Documentation for chemstyle
Version:        svn31096.2.0m

Provides:       tex-chemstyle-doc
AutoReqProv:    No

%description -n texlive-chemstyle-doc
Documentation for chemstyle

%package -n texlive-cherokee
Provides:       tex-cherokee = %{tl_version}
License:        Copyright only
Summary:        A font for the Cherokee script
Version:        svn21046.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cherokee.tfm) = %{tl_version}, tex(cherokee.sty) = %{tl_version}

%description -n texlive-cherokee
The Cherokee script was designed in 1821 by Segwoya. The
alphabet is essentially syllabic, only 6 characters (a e i o s
u) correspond to Roman letters: the font encodes these to the
corresponding roman letter. The remaining 79 characters have
been arbitrarily encoded in the range 38-122; the cherokee
package provides commands that map each such syllable to the
appropriate character; for example, Segwoya himself would be
represented \Cse\Cgwo\Cya. The font is distributed as Metafont
source; it works very poorly in modern environments, and could
do with expert attention (if you are interested, please contact
the CTAN team for details).

%package -n texlive-cherokee-doc
Summary:        Documentation for cherokee
Version:        svn21046.0

Provides:       tex-cherokee-doc
AutoReqProv:    No

%description -n texlive-cherokee-doc
Documentation for cherokee

%package -n texlive-chessboard
Provides:       tex-chessboard = %{tl_version}
License:        LPPL
Summary:        Print chess boards
Version:        svn33801.1.7

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(chessfss.sty), tex(xkeyval.sty), tex(xifthen.sty), tex(ifpdf.sty)
Requires:       tex(tikz.sty), tex(pst-node.sty)
Provides:       tex(chessboard-keys-main.sty) = %{tl_version}
Provides:       tex(chessboard-keys-pgf.sty) = %{tl_version}
Provides:       tex(chessboard-pgf.sty) = %{tl_version}, tex(chessboard.sty) = %{tl_version}

%description -n texlive-chessboard
This package offers commands to print chessboards. It can print
partial boards, hide pieces and fields, color the boards and
put various marks on the board. It has a lot of options to
place pieces on the board. Using exotic pieces (e.g., for fairy
chess) is possible. The documentation includes an example of an
animated chessboard, for those whose PDF viewer can display
animations.

%package -n texlive-chessboard-doc
Summary:        Documentation for chessboard
Version:        svn33801.1.7

Provides:       tex-chessboard-doc
AutoReqProv:    No

%description -n texlive-chessboard-doc
Documentation for chessboard

%package -n texlive-chessfss
Provides:       tex-chessfss = %{tl_version}
License:        LPPL
Summary:        A package to handle chess fonts
Version:        svn19440.1.2a

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(xkeyval.sty)
Provides:       tex(chess-board-example-enc.enc) = %{tl_version}
Provides:       tex(chess-fig-example-enc.enc) = %{tl_version}
Provides:       tex(chessfss.sty) = %{tl_version}, tex(lsb1enc.def) = %{tl_version}
Provides:       tex(lsb1skak.fd) = %{tl_version}, tex(lsb1skaknew.fd) = %{tl_version}
Provides:       tex(lsb2enc.def) = %{tl_version}, tex(lsb2skak.fd) = %{tl_version}
Provides:       tex(lsb2skaknew.fd) = %{tl_version}, tex(lsb3enc.def) = %{tl_version}
Provides:       tex(lsb3skak.fd) = %{tl_version}, tex(lsb3skaknew.fd) = %{tl_version}
Provides:       tex(lsbc1enc.def) = %{tl_version}, tex(lsbc1skaknew.fd) = %{tl_version}
Provides:       tex(lsbc2enc.def) = %{tl_version}, tex(lsbc2skaknew.fd) = %{tl_version}
Provides:       tex(lsbc3enc.def) = %{tl_version}, tex(lsbc3skaknew.fd) = %{tl_version}
Provides:       tex(lsbc4enc.def) = %{tl_version}, tex(lsbc4skaknew.fd) = %{tl_version}
Provides:       tex(lsbc5enc.def) = %{tl_version}, tex(lsbc5skaknew.fd) = %{tl_version}
Provides:       tex(lsbenc.def) = %{tl_version}, tex(lsbskak.fd) = %{tl_version}
Provides:       tex(lsbskaknew.fd) = %{tl_version}, tex(lsfenc.def) = %{tl_version}
Provides:       tex(lsfskak.fd) = %{tl_version}, tex(lsfskaknew.fd) = %{tl_version}
Provides:       tex(lsienc.def) = %{tl_version}, tex(lsiskak.fd) = %{tl_version}
Provides:       tex(lsiskaknew.fd) = %{tl_version}

%description -n texlive-chessfss
This package offers commands to use and switch between chess
fonts. It uses the LaTeX font selection scheme (nfss). The
package doesn't parse, format and print PGN input like e.g. the
packages skak or texmate; the aim of the package is to offer
writers of chess packages a bundle of commands for fonts, so
that they don't have to implement all these commands for
themselves. A normal user can use the package to print e.g.
single chess symbols and simple diagrams. The documentation
contains also a section about installation of chess fonts.

%package -n texlive-chessfss-doc
Summary:        Documentation for chessfss
Version:        svn19440.1.2a

Provides:       tex-chessfss-doc
AutoReqProv:    No

%description -n texlive-chessfss-doc
Documentation for chessfss

%package -n texlive-chess-problem-diagrams
Provides:       tex-chess-problem-diagrams = %{tl_version}
License:        LPPL 1.2
Summary:        A package for typesetting chess problem diagrams
Version:        svn39317

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(calc.sty), tex(pstricks.sty)
Provides:       tex(diagram.sty) = %{tl_version}

%description -n texlive-chess-problem-diagrams
This package provides macros to typeset chess problem diagrams
including fairy chess problems (mostly using rotated images of
pieces) and other boards.

%package -n texlive-chess-problem-diagrams-doc
Summary:        Documentation for chess-problem-diagrams
Version:        svn39317

Provides:       tex-chess-problem-diagrams-doc
AutoReqProv:    No

%description -n texlive-chess-problem-diagrams-doc
Documentation for chess-problem-diagrams

%package -n texlive-chess
Provides:       tex-chess = %{tl_version}
License:        Public Domain
Summary:        Fonts for typesetting chess boards
Version:        svn20582.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chess10.tfm) = %{tl_version}, tex(chess20.tfm) = %{tl_version}
Provides:       tex(chess30.tfm) = %{tl_version}, tex(chessf10.tfm) = %{tl_version}
Provides:       tex(chessfig10.tfm) = %{tl_version}, tex(chess.sty) = %{tl_version}

%description -n texlive-chess
The original (and now somewhat dated) TeX chess font package.
Potential users should consider skak (for alternative fonts,
and notation support), texmate (for alternative notation
support), or chessfss (for flexible font choices).

%package -n texlive-chess-doc
Summary:        Documentation for chess
Version:        svn20582.1.2

Provides:       tex-chess-doc
AutoReqProv:    No

%description -n texlive-chess-doc
Documentation for chess

%package -n texlive-chet
Provides:       tex-chet = %{tl_version}
License:        LPPL 1.3
Summary:        LaTeX layout inspired by harvmac
Version:        svn45081
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(kvoptions.sty)
Provides:       tex(chet.sty) = %{tl_version}

%description -n texlive-chet
The package aims to streamline the work of typesetting, and to
provide the look and feel of harvmac for readers.

%package -n texlive-chet-doc
Summary:        Documentation for chet
Version:        svn45081
Provides:       tex-chet-doc
AutoReqProv:    No

%description -n texlive-chet-doc
Documentation for chet

%package -n texlive-chextras
Provides:       tex-chextras = %{tl_version}
License:        LPPL 1.3
Summary:        A companion package for the Swiss typesetter
Version:        svn27118.1.01

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(inputenc.sty), tex(luainputenc.sty), tex(xunicode.sty), tex(fixltx2e.sty)
Requires:       tex(fontenc.sty), tex(lmodern.sty), tex(babel.sty), tex(etoolbox.sty)
Requires:       tex(xkeyval.sty), tex(makecmds.sty), tex(hyperref.sty)
Provides:       tex(chextras.sty) = %{tl_version}, tex(eu1lmros.fd) = %{tl_version}
Provides:       tex(eu1lmssos.fd) = %{tl_version}, tex(eu1lmttos.fd) = %{tl_version}
Provides:       tex(eu1lmvttos.fd) = %{tl_version}, tex(t1lmros.fd) = %{tl_version}
Provides:       tex(t1lmssos.fd) = %{tl_version}, tex(t1lmttos.fd) = %{tl_version}
Provides:       tex(t1lmvttos.fd) = %{tl_version}

%description -n texlive-chextras
The package simplifies the preparation of Swiss documents and
letters by setting up linguistic and common packages. While it
is a useful addition to the chletter document class, it is not
tied to it and may be used as a general purpose package.

%package -n texlive-chextras-doc
Summary:        Documentation for chextras
Version:        svn27118.1.01

Provides:       tex-chextras-doc
AutoReqProv:    No

%description -n texlive-chextras-doc
Documentation for chextras

%package -n texlive-chicago-annote
Provides:       tex-chicago-annote = %{tl_version}
License:        LPPL
Summary:        Chicago-based annotated BibTeX style
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea


%description -n texlive-chicago-annote
This is a revision of chicagoa.bst, using the commonly-used
annote field in place of the original's annotation.

%package -n texlive-chicago-annote-doc
Summary:        Documentation for chicago-annote
Version:        svn15878.0

Provides:       tex-chicago-annote-doc
AutoReqProv:    No

%description -n texlive-chicago-annote-doc
Documentation for chicago-annote

%package -n texlive-chicago
Provides:       tex-chicago = %{tl_version}
License:        Knuth
Summary:        A "Chicago" bibliography style
Version:        svn15878.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chicago.sty) = %{tl_version}

%description -n texlive-chicago
Chicago is a BibTeX style that follows the "B" reference style
of the 13th Edition of the Chicago manual of style; a LaTeX
package (to LaTeX 2.09 conventions) is also provided. The style
was derived from the newapa style.

%package -n texlive-chickenize
Provides:       tex-chickenize = %{tl_version}
License:        LPPL 1.3
Summary:        Use lua callbacks for "interesting" textual effects
Version:        svn45083
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(chickenize.sty) = %{tl_version}, tex(chickenize.tex) = %{tl_version}

%description -n texlive-chickenize
The package allows manipulations of any LuaTeX document (it is
known to work with Plain LuaTeX and LuaLaTeX). Most of the
package's functions are merely for fun or educational use, but
some functions (for example, colorstretch for visualising the
badness and font expansion of each line, and letterspaceadjust
doing what its name says) could be useful in a "normal" LuaTeX
document.

%package -n texlive-chickenize-doc
Summary:        Documentation for chickenize
Version:        svn45083
Provides:       tex-chickenize-doc
AutoReqProv:    No

%description -n texlive-chickenize-doc
Documentation for chickenize

%package -n texlive-chkfloat
Provides:       tex-chkfloat = %{tl_version}
License:        LPPL 1.3
Summary:        Warn whenever a float is placed "to far away"
Version:        svn27473.0.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(kvoptions.sty)
Provides:       tex(chkfloat.sty) = %{tl_version}

%description -n texlive-chkfloat
The package checks for floats that are placed too far from
their origin. It was motivated by a question on the question
and answer page.

%package -n texlive-chkfloat-doc
Summary:        Documentation for chkfloat
Version:        svn27473.0.1

Provides:       tex-chkfloat-doc
AutoReqProv:    No

%description -n texlive-chkfloat-doc
Documentation for chkfloat

%package -n texlive-chletter
Provides:       tex-chletter = %{tl_version}
License:        LPPL
Summary:        Class for typesetting letters to Swiss rules
Version:        svn20060.2.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chletter.cls) = %{tl_version}

%description -n texlive-chletter
The class enables composition of letters fitting into Swiss C5
& C6/5 windowed envelopes. No assumption is made about the
language used. The class is based on the standard LaTeX classes
and is compatible with the LaTeX letter class. It is not
limited to letters and may be used as a generic document class;
it is used with the chextras package.

%package -n texlive-chletter-doc
Summary:        Documentation for chletter
Version:        svn20060.2.0

Provides:       tex-chletter-doc
AutoReqProv:    No

%description -n texlive-chletter-doc
Documentation for chletter

%package -n texlive-chngcntr
Provides:       tex-chngcntr = %{tl_version}
License:        LPPL
Summary:        Change the resetting of counters
Version:        svn47577
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(chngcntr.sty) = %{tl_version}

%description -n texlive-chngcntr
Defines commands \counterwithin (which sets up a counter to be
reset when another is incremented) and \counterwithout (which
unsets such a relationship).

%package -n texlive-chngcntr-doc
Summary:        Documentation for chngcntr
Version:        svn47577
Provides:       tex-chngcntr-doc
AutoReqProv:    No

%description -n texlive-chngcntr-doc
Documentation for chngcntr

%package -n texlive-chronology
Provides:       tex-chronology = %{tl_version}
License:        LPPL 1.3
Summary:        Provides a horizontal timeline
Version:        svn37934.1.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(calc.sty), tex(tikz.sty), tex(xparse.sty)
Provides:       tex(chronology.sty) = %{tl_version}

%description -n texlive-chronology
A timeline package that allows labelling of events with per-day
granularity. Other features include relative positioning with
unit specification, adjustable tick mark step size, and scaling
to specified width.

%package -n texlive-chronology-doc
Summary:        Documentation for chronology
Version:        svn37934.1.1.1

Provides:       tex-chronology-doc
AutoReqProv:    No

%description -n texlive-chronology-doc
Documentation for chronology

%package -n texlive-chronosys
Provides:       tex-chronosys = %{tl_version}
License:        LPPL 1.3
Summary:        Drawing time-line diagrams
Version:        svn26700.1.2

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(tikz.sty)
Provides:       tex(chronosys.sty) = %{tl_version}, tex(chronosys.tex) = %{tl_version}
Provides:       tex(chronosyschr.tex) = %{tl_version}, tex(x-chronosys.tex) = %{tl_version}

%description -n texlive-chronosys
Macros to produce time line diagrams. Interfaces for Plain TeX,
Context and LaTeX are provided.

%package -n texlive-chronosys-doc
Summary:        Documentation for chronosys
Version:        svn26700.1.2

Provides:       tex-chronosys-doc
AutoReqProv:    No

%description -n texlive-chronosys-doc
Documentation for chronosys

%package -n texlive-chscite
Provides:       tex-chscite = %{tl_version}
License:        LPPL 1.2
Summary:        Bibliography style for Chalmers University of Technology
Version:        svn28552.2.9999

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Requires:       tex(ifthen.sty), tex(url.sty)
Provides:       tex(chscite.sty) = %{tl_version}

%description -n texlive-chscite
The package, heavily based on the harvard package for Harvard-
style citations, provides a citation suite for students at
Chalmers University of Technology that follows given
recommendations.

%package -n texlive-chscite-doc
Summary:        Documentation for chscite
Version:        svn28552.2.9999

Provides:       tex-chscite-doc
AutoReqProv:    No

%description -n texlive-chscite-doc
Documentation for chscite

%package -n texlive-cinzel
Provides:       tex-cinzel = %{tl_version}
License:        OFL
Summary:        LaTeX support for Cinzel and Cinzel Decorative fonts
Version:        svn34408.0

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       texlive-tetex-bin, tex-tetex


Requires:       tex(ifxetex.sty), tex(ifluatex.sty), tex(xkeyval.sty), tex(textcomp.sty)
Requires:       tex(fontspec.sty), tex(fontenc.sty), tex(fontaxes.sty), tex(mweights.sty)
Provides:       tex(cnzl_7luz43.enc) = %{tl_version}, tex(cnzl_7t2zcj.enc) = %{tl_version}
Provides:       tex(cnzl_aakhvz.enc) = %{tl_version}, tex(cnzl_k6z3ge.enc) = %{tl_version}
Provides:       tex(cinzel.map) = %{tl_version}, tex(Cinzel-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-t1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-t1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ts1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ly1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ly1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ot1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-t1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-t1.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ts1--base.tfm) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ts1.tfm) = %{tl_version}
Provides:       tex(Cinzel-Black.ttf) = %{tl_version}, tex(Cinzel-Bold.ttf) = %{tl_version}
Provides:       tex(Cinzel-Regular.ttf) = %{tl_version}, tex(CinzelDecorative-Black.ttf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold.ttf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular.ttf) = %{tl_version}
Provides:       tex(Cinzel-Black.pfb) = %{tl_version}, tex(Cinzel-Bold.pfb) = %{tl_version}
Provides:       tex(Cinzel-Regular.pfb) = %{tl_version}, tex(CinzelDecorative-Black.pfb) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold.pfb) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular.pfb) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(Cinzel-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(Cinzel-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(Cinzel-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ly1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-t1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Black-lf-ts1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ly1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-t1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Bold-lf-ts1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ly1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-t1.vf) = %{tl_version}
Provides:       tex(CinzelDecorative-Regular-lf-ts1.vf) = %{tl_version}
Provides:       tex(LY1Cinzel-LF.fd) = %{tl_version}, tex(LY1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(OT1Cinzel-LF.fd) = %{tl_version}, tex(OT1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(T1Cinzel-LF.fd) = %{tl_version}, tex(T1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(TS1Cinzel-LF.fd) = %{tl_version}, tex(TS1CinzelDecorative-LF.fd) = %{tl_version}
Provides:       tex(cinzel.sty) = %{tl_version}

%description -n texlive-cinzel
Cinzel and Cinzel Decorative fonts, designed by Natanael Gama
Natanael Gama), find their inspiration in first century roman
inscriptions, and are based on classical proportions. Cinzel is
all-caps (similar to Trajan and Michelangelo), but is available
in three weights (Regular, Bold, Black). There are no italic
fonts, but there are Decorative variants, which can be selected
by the usual italic-selection commands in the package's LaTeX
support.

%package -n texlive-cinzel-doc
Summary:        Documentation for cinzel
Version:        svn34408.0

Provides:       tex-cinzel-doc
AutoReqProv:    No

%description -n texlive-cinzel-doc
Documentation for cinzel

%package -n texlive-circ
Provides:       tex-circ = %{tl_version}
License:        GPL+
Summary:        Macros for typesetting circuit diagrams
Version:        svn15878.1.1

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(cioptic.tfm) = %{tl_version}, tex(basic.def) = %{tl_version}
Provides:       tex(box.def) = %{tl_version}, tex(circ.sty) = %{tl_version}
Provides:       tex(gate.def) = %{tl_version}, tex(ic.def) = %{tl_version}
Provides:       tex(oldgate.def) = %{tl_version}, tex(optics.def) = %{tl_version}
Provides:       tex(physics.def) = %{tl_version}

%description -n texlive-circ
Several electrical symbols like resistor, capacitor,
transistors etc., are defined. The symbols can be connected
with wires. The package also contains an American resistor
symbol for those of us on that side of the Atlantic. The
package also has simple facilities for producing optics
diagrams; however, no-one would deny that the PSTricks pst-
optic package, or the MetaPost makecirc package does the job
better.

%package -n texlive-circ-doc
Summary:        Documentation for circ
Version:        svn15878.1.1

Provides:       tex-circ-doc
AutoReqProv:    No

%description -n texlive-circ-doc
Documentation for circ

%package -n texlive-circuitikz
Provides:       tex-circuitikz = %{tl_version}
License:        LPPL
Summary:        Draw electrical networks with TikZ
Version:        svn44488
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(tikz.sty), tex(xstring.sty), tex(siunitx.sty)
Provides:       tex(t-circuitikz.tex) = %{tl_version}, tex(circuitikz.code.tex) = %{tl_version}
Provides:       tex(circuitikz1.code.tex) = %{tl_version}
Provides:       tex(pgfcircbipoles.tex) = %{tl_version}, tex(pgfcirccurrent.tex) = %{tl_version}
Provides:       tex(pgfcircinputarrows.tex) = %{tl_version}
Provides:       tex(pgfcirclabel.tex) = %{tl_version}, tex(pgfcircmath.tex) = %{tl_version}
Provides:       tex(pgfcircmonopoles.tex) = %{tl_version}
Provides:       tex(pgfcircnpoles.tex) = %{tl_version}, tex(pgfcircquadpoles.tex) = %{tl_version}
Provides:       tex(pgfcircshapes.tex) = %{tl_version}, tex(pgfcirctripoles.tex) = %{tl_version}
Provides:       tex(pgfcircutils.tex) = %{tl_version}, tex(pgfcircvoltage.tex) = %{tl_version}
Provides:       tex(circuitikz.sty) = %{tl_version}

%description -n texlive-circuitikz
The package provides a set of macros for naturally typesetting
electrical and (somewhat less naturally, perhaps) electronic
networks. It is designed as a tool that is easy to use, with a
lean syntax, native to LaTeX, and directly supporting PDF
output format. So is based on the very impressive pgf/TikZ
package.

%package -n texlive-circuitikz-doc
Summary:        Documentation for circuitikz
Version:        svn44488
Provides:       tex-circuitikz-doc
AutoReqProv:    No

%description -n texlive-circuitikz-doc
Documentation for circuitikz

%package -n texlive-citeall
Provides:       tex-citeall = %{tl_version}
License:        LPPL 1.3
Summary:        Cite all entries of a bbl created with biblatex
Version:        svn45975
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Requires:       tex(expl3.sty), tex(xparse.sty)
Provides:       tex(citeall.sty) = %{tl_version}

%description -n texlive-citeall
This small package allows to cite all entries of a bbl-file
created with biblatex (v1.9).

%package -n texlive-citeall-doc
Summary:        Documentation for citeall
Version:        svn45975
Provides:       tex-citeall-doc
AutoReqProv:    No

%description -n texlive-citeall-doc
Documentation for citeall

%package -n texlive-cite
Provides:       tex-cite = %{tl_version}
License:        Copyright only
Summary:        Improved citation handling in LaTeX
Version:        svn36428.5.5

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(chapterbib.sty) = %{tl_version}, tex(cite.sty) = %{tl_version}
Provides:       tex(drftcite.sty) = %{tl_version}, tex(overcite.sty) = %{tl_version}

%description -n texlive-cite
The package supports compressed, sorted lists of numerical
citations, and also deals with various punctuation and other
issues of representation, including comprehensive management of
break points. The package is compatible with both hyperref and
backref. The package is (unsurprisingly) part of the cite
bundle of the author's citation-related packages.

%package -n texlive-cite-doc
Summary:        Documentation for cite
Version:        svn36428.5.5

Provides:       tex-cite-doc
AutoReqProv:    No

%description -n texlive-cite-doc
Documentation for cite

%package -n texlive-breakcites-doc
Provides:       tex-breakcites-doc = %{tl_version}
License:        Copyright only
Summary:        doc files of breakcites
Version:        svn21014

AutoReqProv:    No

%description -n texlive-breakcites-doc
Documentation for breakcites
   
%package -n texlive-breakcites
Provides:       tex-breakcites = %{tl_version}
License:        Copyright only
Summary:        Ensure that multiple citations may break at line end
Version:        svn21014

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(breakcites.sty) = %{tl_version}

%description -n texlive-breakcites
Makes a very minor change to the operation of the \cite
command. Note that the change is not necessary in unmodified
LaTeX; however, there remain packages that restore the
undesirable behaviour of the command as provided in LaTeX 2.09.
(Note that neither cite nor natbib make this mistake.)

%package -n texlive-bxdvidriver-doc
Provides:       tex-bxdvidriver-doc = %{tl_version}
License:        MIT
Summary:        doc files of bxdvidriver
Version:        svn43219
AutoReqProv:    No

%description -n texlive-bxdvidriver-doc
Documentation for bxdvidriver

%package -n texlive-bxdvidriver
Provides:       tex-bxdvidriver = %{tl_version}
License:        MIT
Summary:        Enables specifying a driver option effective only in DVI output
Version:        svn43219
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bxdvidriver.sty) = %{tl_version}

%description -n texlive-bxdvidriver
This single-function package enables authors to specify a
global driver option (dvips, dvipdfmx, etc) which is applied
only when the engine outputs a DVI file. It is useful to create
special document- templates that can be compiled in both PDF-
mode and DVI-mode.

%package -n texlive-bxenclose-doc
Provides:       tex-bxenclose-doc = %{tl_version}
License:        MIT
Summary:        doc files of bxenclose
Version:        svn40213

AutoReqProv:    No

%description -n texlive-bxenclose-doc
Documentation for bxenclose

%package -n texlive-bxenclose
Provides:       tex-bxenclose = %{tl_version}
License:        MIT
Summary:        Enclose the document body with some pieces of code
Version:        svn40213

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(bxenclose.sty) = %{tl_version}

%description -n texlive-bxenclose
The package enables authors to designate in the preamble to
make the document body enclosed with the given pieces of code.
As is known, there are already various mechanisms provided by
LaTeX kernel or packages that attach hooks at the beginning and
end of documents.

%package -n texlive-bxnewfont-doc
Provides:       tex-bxnewfont-doc = %{tl_version}
License:        MIT
Summary:        doc files of bxnewfont
Version:        svn44173
AutoReqProv:    No

%description -n texlive-bxnewfont-doc
Documentation for bxnewfont

%package -n texlive-bxnewfont
Provides:       tex-bxnewfont = %{tl_version}
License:        MIT
Summary:        Enhanced \newfont command
Version:        svn44173
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bxnewfont.sty) = %{tl_version}

%description -n texlive-bxnewfont
This package provides a new command \newfontx. It is similar to
the old (and deprecated) command \newfont in function, but is
more compatible with NFSS. In particular, one can safely change
font size after invoking a font command defined by \newfontx.
The new command will be useful to users who know much of the
old \newfont command but are unfamiliar with the detail of
NFSS.

%package -n texlive-bxpapersize-doc
Provides:       tex-bxpapersize-doc = %{tl_version}
License:        MIT
Summary:        doc files of bxpapersize
Version:        svn45501
AutoReqProv:    No

%description -n texlive-bxpapersize-doc
Documentation for bxpapersize

%package -n texlive-bxpapersize
Provides:       tex-bxpapersize = %{tl_version}
License:        MIT
Summary:        Synchronize output paper size with layout paper size
Version:        svn45501
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(bxpapersize.sty) = %{tl_version}

%description -n texlive-bxpapersize
As is well known, in LaTeX processing layout paper size
specified by document class options is not automatically
applied to output paper size. This package enables LaTeX
authors to synchronize both kinds of paper sizes.

%package -n texlive-carbohydrates-doc
Provides:       tex-carbohydrates-doc = %{tl_version}
License:        LPPL
Summary:        doc files of carbohydrates
Version:        svn39000

AutoReqProv:    No

%description -n texlive-carbohydrates-doc
Documentation for carbohydrates

%package -n texlive-carbohydrates
Provides:       tex-carbohydrates = %{tl_version}
License:        LPPL
Summary:        Carbohydrate molecules with chemfig
Version:        svn39000

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(carbohydrates.sty) = %{tl_version}

%description -n texlive-carbohydrates
This package offers macros that make the preparation of
exercise sheets for teaching carbohydrate chemistry a lot less
tedious. It uses chemfig for drawing the formulas. Different
representation models (Fischer, Haworth, chair...) are
supported as well as alpha, beta, and chain isomers.

%package -n texlive-chivo-doc
Provides:       tex-chivo-doc = %{tl_version}
License:        LPPL
Summary:        doc files of chivo
Version:        svn40931

AutoReqProv:    No

%description -n texlive-chivo-doc
Documentation for chivo

%package -n texlive-chivo
Provides:       tex-chivo = %{tl_version}
License:        LPPL
Summary:        Using the free Chivo fonts with LaTeX
Version:        svn40931

Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea

Provides:       tex(Chivo.sty) = %{tl_version}, tex(Chivo.map) = %{tl_version}
Provides:       tex(OT1Chivo-TLF.fd) = %{tl_version}, tex(TS1Chivo-TLF.fd) = %{tl_version}
Provides:       tex(T1Chivo-TLF.fd) = %{tl_version}, tex(LY1Chivo-TLF.fd) = %{tl_version}
Provides:       tex(Chivo-RegularLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-ItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-LightLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-Light.pfb) = %{tl_version}, tex(Chivo-BlackLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-BlackItalic.pfb) = %{tl_version}
Provides:       tex(Chivo-BoldLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-Regular.pfb) = %{tl_version}, tex(Chivo-Italic.pfb) = %{tl_version}
Provides:       tex(Chivo-BlackItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-Black.pfb) = %{tl_version}, tex(Chivo-BoldItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(Chivo-BoldItalic.pfb) = %{tl_version}
Provides:       tex(Chivo-Bold.pfb) = %{tl_version}, tex(Chivo-LightItalic.pfb) = %{tl_version}
Provides:       tex(Chivo-LightItalicLCDFJ.pfb) = %{tl_version}
Provides:       tex(chi_g7gdou.enc) = %{tl_version}, tex(chi_qbau2s.enc) = %{tl_version}
Provides:       tex(chi_hxspk6.enc) = %{tl_version}, tex(chi_m6it5z.enc) = %{tl_version}
Provides:       tex(Chivo-Light.otf) = %{tl_version}, tex(Chivo-Regular.otf) = %{tl_version}
Provides:       tex(Chivo-Italic.otf) = %{tl_version}, tex(Chivo-LightItalic.otf) = %{tl_version}
Provides:       tex(Chivo-BlackItalic.otf) = %{tl_version}
Provides:       tex(Chivo-BoldItalic.otf) = %{tl_version}
Provides:       tex(Chivo-Bold.otf) = %{tl_version}, tex(Chivo-Black.otf) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ly1.vf) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ts1.vf) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-t1.vf) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ot1.vf) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ot1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-t1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BoldItalic-tlf-ly1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ot1--lcdfj.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Black-tlf-ot1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ts1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ly1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-LightItalic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-Italic-tlf-ly1.tfm) = %{tl_version}
Provides:       tex(Chivo-Bold-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-BlackItalic-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-t1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-ts1.tfm) = %{tl_version}
Provides:       tex(Chivo-Light-tlf-t1--base.tfm) = %{tl_version}
Provides:       tex(Chivo-Regular-tlf-ly1--base.tfm) = %{tl_version}

%description -n texlive-chivo
This work provides the necessary files to use the Chivo fonts
with LaTeX. Chivo is a set of eight fonts provided by Hector
Gatti & Omnibus Team under the Open Font License
[(OFL)](http://scripts.sil.org/OFL), version 1.1. The fonts are
copyright (c) 2011-2015, Omnibus-Type.

%package -n texlive-churchslavonic-doc
Provides:       tex-churchslavonic-doc = %{tl_version}
License:        MIT
Summary:        doc files of churchslavonic
Version:        svn42751
AutoReqProv:    No

%description -n texlive-churchslavonic-doc
Documentation for churchslavonic

%package -n texlive-churchslavonic
Provides:       tex-churchslavonic = %{tl_version}
License:        MIT
Summary:        Typesetting documents in Church Slavonic language using Unicode
Version:        svn42751
Requires:       texlive-base, texlive-kpathsea-bin, tex-kpathsea
Provides:       tex(cu-util.sty) = %{tl_version}, tex(cu-kinovar.sty) = %{tl_version}
Provides:       tex(churchslavonic.sty) = %{tl_version}, tex(cu-num.sty) = %{tl_version}
Provides:       tex(cu-calendar.sty) = %{tl_version}

%description -n texlive-churchslavonic
The package provides fonts, hyphenation patterns and supporting
macros to typeset Church Slavonic texts.


%package -n texlive-bredzenie
Summary:        a Polish version of "lorem ipsum..." in the form of a LaTeX package
Version:        svn44371
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bredzenie.sty) = %{tl_version}

%description -n texlive-bredzenie
This is a polish version of the classic pseudo-Latin "lorem
ipsum dolor sit amet...". It provides access to several
paragraphs of pseudo-Polish generated with Hidden Markov Models
and Recurrent Neural Networks trained on a corpus of Polish.

%package -n texlive-bxcalc
Summary:        To extend the functionality of the calc package
Version:        svn46482
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bxcalc.sty) = %{tl_version}, tex(bxcalcize.sty) = %{tl_version}
Provides:       tex(bxcalcux.sty) = %{tl_version}

%description -n texlive-bxcalc
This package bundle consists of the following packages:
bxcalcize: To make calc expressions available in more places.
bxcalcux: To add user-defined units to the calc syntax. In
addition, this bundle provides the bxcalc package, which simply
loads the above-mentioned packages internally.

%package -n texlive-bxjalipsum
Summary:        Dummy text in Japanese
Version:        svn43369
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bxjalipsum.sty) = %{tl_version}

%description -n texlive-bxjalipsum
This package enables users to print some Japanese text that can
be used as dummy text. It is a Japanese counterpart of the
lipsum package. Since there is no well-known nonsense text like
Lipsum in the Japanese language, the package uses some real
text in public domain.

%package -n texlive-bxjaprnind
Summary:        Adjust the position of parentheses at paragraph head
Version:        svn45291
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bxjaprnind.sty) = %{tl_version}

%description -n texlive-bxjaprnind
In Japanese typesetting, opening parentheses placed at the
beginning of paragraphs or lines are treated specially; for
example, while the paragraph indent before normal kanji
characters is 1em, the indent before parentheses can be 0.5em,
1em or 1.5em deoending on the local rule in effect.

%package -n texlive-bxorigcapt
Summary:        To retain the original caption names when using Babel
Version:        svn44195
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(bxorigcapt.sty) = %{tl_version}

%description -n texlive-bxorigcapt
This package forces the caption names (`\chaptername`,
`\today`, etc) declared by the document class in use to be used
as the caption names for a specific language introduced by the
Babel package.

%package -n texlive-callouts
Summary:        Put simple annotations and notes inside a picture
Version:        svn44899
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(callouts.sty) = %{tl_version}

%description -n texlive-callouts
The package defines the annotation environment in which
callouts, notes, arrows, and the like can be placed to describe
certain parts of a picture.

%package -n texlive-cesenaexam
Summary:        A class file to typeset exams
Version:        svn44960
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cesenaexam.cls) = %{tl_version}, tex(cesenaexam.sty) = %{tl_version}

%description -n texlive-cesenaexam
This LaTeX document class has been designed to typeset exams.

%package -n texlive-cheatsheet
Summary:        A simple cheatsheet class
Version:        svn45069
License:        MIT
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cheatsheet.cls) = %{tl_version}

%description -n texlive-cheatsheet
The package provides a clean, multi-column design intended for
cheat sheets. It imports the most useful packages and encloses
the document in a multicol environment.

%package -n texlive-childdoc
Summary:        directly compile \include'd child documents
Version:        svn46357
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(childdoc.def) = %{tl_version}

%description -n texlive-childdoc
childdoc is a LaTeX2e package that enables the direct
compilation of document sections included by \include to
individual files.

%package -n texlive-cascade
Summary:        Constructions with braces to present mathematical demonstrations
Version:        svn48200
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(cascade.sty) = %{tl_version}

%description -n texlive-cascade
The LaTeX package cascade provides a command \Cascade to do
constructions to present mathematical demonstrations with
successive braces for the deductions.

%package -n texlive-cellprops
Summary:        Accept CSS-like selectors in tabular, array, ...
Version:        svn48227
License:        GPLv3+
Requires:       texlive-base texlive-kpathsea, tex(mdwtab.sty)
Requires:       tex(xcolor.sty), tex(expl3.sty), tex(xparse.sty)
Provides:       tex(cellprops.sty) = %{tl_version}

%description -n texlive-cellprops
This package reworks the internals of tabular, array, and
similar constructs, and adds a \cellprops command accepting
CSS-like selectors and properties. It depends on mdwtab,
xcolor, expl3, and xparse.

%package -n texlive-chemsec
Summary:        Automated creation of numeric entity labels
Version:        svn46972
License:        LPPL
Requires:       texlive-base texlive-kpathsea
Provides:       tex(chemsec.sty) = %{tl_version}

%description -n texlive-chemsec
Packages provides creation of sequential numeric labels for
entities in a document. The motivating example is chemical
structures in a scientific document. The package can
automatically output a full object name and label on the first
occurence in the document and just labels only on subsequent
references.

%prep
%setup -q -c -T -a 3

%build

%install
install -d %{buildroot}%{_texdir}/../texmf
install -d %{buildroot}%{_texdir}/texmf-config/web2c
install -d %{buildroot}%{_var}/lib/texmf
install -d %{buildroot}%{_texdir}/texmf-dist
install -d %{buildroot}%{_texdir}/texmf-local

set +x
for i in %{sources}; do
  if [ "$i" != "%{_sourcedir}/texlive-licenses.tar.xz" ]; then
    if [ "$i" = "%{_sourcedir}/texlive-msg-translations.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.tar.xz" -o \
         "$i" = "%{_sourcedir}/xecyr.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.tar.xz" -o \
         "$i" = "%{_sourcedir}/platex.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/texworks.doc.tar.xz" -o \
         "$i" = "%{_sourcedir}/uplatex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.tar.xz" -o \
         "$i" = "%{_sourcedir}/texlive-docindex.doc.tar.xz" ]; then
      OUTDIR="%{buildroot}%{_texdir}"
    else
      OUTDIR="%{buildroot}%{_texdir}/texmf-dist"
    fi
    xz -dc $i | tar x -C $OUTDIR
  fi
done
set -x

cur_dir=$PWD


install -d %{buildroot}%{_datadir}/fonts
cd %{buildroot}%{_datadir}/fonts
font_names="impallari/cabin public/ccicons"
for i in ${font_names}; do
  j=`echo $i | cut -d / -f 2`
  ln -s %{_texdir}/texmf-dist/fonts/opentype/$i $j
done
cd $cur_dir


install -d %{buildroot}/%{_infodir}/
rm -f %{buildroot}%{_datadir}/texlive/texmf-dist/tlpkg/tlpobj/*


%files -n texlive-blacklettert1
%{_texdir}/texmf-dist/fonts/tfm/public/blacklettert1/
%{_texdir}/texmf-dist/fonts/vf/public/blacklettert1/
%{_texdir}/texmf-dist/tex/latex/blacklettert1/

%files -n texlive-blacklettert1-doc
%{_texdir}/texmf-dist/doc/fonts/blacklettert1/

%files -n texlive-blindtext
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/blindtext/

%files -n texlive-blindtext-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/blindtext/

%files -n texlive-blkarray
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/blkarray/

%files -n texlive-blkarray-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/blkarray/

%files -n texlive-blochsphere
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/blochsphere/

%files -n texlive-blochsphere-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/blochsphere/

%files -n texlive-blockdraw_mp
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/blockdraw_mp/

%files -n texlive-blockdraw_mp-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/blockdraw_mp/

%files -n texlive-block
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/block/

%files -n texlive-block-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/block/

%files -n texlive-bloques
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bloques/

%files -n texlive-bloques-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bloques/

%files -n texlive-blox
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/blox/

%files -n texlive-blox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/blox/

%files -n texlive-bnumexpr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bnumexpr/

%files -n texlive-bnumexpr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bnumexpr/

%files -n texlive-bodegraph
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bodegraph/

%files -n texlive-bodegraph-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bodegraph/

%files -n texlive-bohr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bohr/

%files -n texlive-bohr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bohr/

%files -n texlive-boisik
%license gpl2.txt
%{_texdir}/texmf-dist/fonts/source/public/boisik/
%{_texdir}/texmf-dist/fonts/tfm/public/boisik/
%{_texdir}/texmf-dist/tex/latex/boisik/

%files -n texlive-boisik-doc
%license gpl2.txt
%{_texdir}/texmf-dist/doc/fonts/boisik/

%files -n texlive-boites
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/boites/

%files -n texlive-boites-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/boites/

%files -n texlive-bold-extra
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bold-extra/

%files -n texlive-bold-extra-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bold-extra/

%files -n texlive-boldtensors
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/boldtensors/

%files -n texlive-boldtensors-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/boldtensors/

%files -n texlive-bondgraphs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bondgraphs/

%files -n texlive-bondgraphs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bondgraphs/

%files -n texlive-bondgraph
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bondgraph/

%files -n texlive-bondgraph-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bondgraph/

%files -n texlive-bookcover
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/bookcover/

%files -n texlive-bookcover-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/bookcover/

%files -n texlive-bookdb
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/bookdb/

%files -n texlive-bookdb-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/bibtex/bookdb/

%files -n texlive-bookest
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bookest/

%files -n texlive-bookest-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bookest/

%files -n texlive-bookhands
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/bookhands/
%{_texdir}/texmf-dist/fonts/map/dvips/bookhands/
%{_texdir}/texmf-dist/fonts/source/public/bookhands/
%{_texdir}/texmf-dist/fonts/tfm/public/bookhands/
%{_texdir}/texmf-dist/fonts/type1/public/bookhands/
%{_texdir}/texmf-dist/tex/latex/bookhands/

%files -n texlive-bookhands-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/bookhands/

%files -n texlive-booklet
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/booklet/

%files -n texlive-booklet-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/booklet/

%files -n texlive-bookman
%license gpl.txt
%{_texdir}/texmf-dist/dvips/bookman/
%{_texdir}/texmf-dist/fonts/afm/adobe/bookman/
%{_texdir}/texmf-dist/fonts/afm/urw/bookman/
%{_texdir}/texmf-dist/fonts/map/dvips/bookman/
%{_texdir}/texmf-dist/fonts/tfm/adobe/bookman/
%{_texdir}/texmf-dist/fonts/tfm/urw35vf/bookman/
%{_texdir}/texmf-dist/fonts/type1/urw/bookman/
%{_texdir}/texmf-dist/fonts/vf/adobe/bookman/
%{_texdir}/texmf-dist/fonts/vf/urw35vf/bookman/
%{_texdir}/texmf-dist/tex/latex/bookman/

%files -n texlive-booktabs-de-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/booktabs-de/

%files -n texlive-booktabs-fr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/booktabs-fr/

%files -n texlive-booktabs
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/booktabs/

%files -n texlive-booktabs-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/booktabs/

%files -n texlive-boolexpr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/boolexpr/

%files -n texlive-boolexpr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/boolexpr/

%files -n texlive-boondox
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/boondox/
%{_texdir}/texmf-dist/fonts/tfm/public/boondox/
%{_texdir}/texmf-dist/fonts/type1/public/boondox/
%{_texdir}/texmf-dist/fonts/vf/public/boondox/
%{_texdir}/texmf-dist/tex/latex/boondox/

%files -n texlive-boondox-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/boondox/

%files -n texlive-bophook
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bophook/

%files -n texlive-bophook-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bophook/

%files -n texlive-borceux
%{_texdir}/texmf-dist/tex/generic/borceux/

%files -n texlive-borceux-doc
%{_texdir}/texmf-dist/doc/generic/borceux/

%files -n texlive-bosisio
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bosisio/

%files -n texlive-bosisio-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bosisio/

%files -n texlive-boxedminipage2e
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/boxedminipage2e/

%files -n texlive-boxedminipage2e-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/boxedminipage2e/

%files -n texlive-boxedminipage
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/boxedminipage/

%files -n texlive-boxedminipage-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/boxedminipage/

%files -n texlive-boxhandler
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/boxhandler/

%files -n texlive-boxhandler-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/boxhandler/

%files -n texlive-bpchem
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bpchem/

%files -n texlive-bpchem-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bpchem/

%files -n texlive-bpolynomial
%license lppl1.txt
%{_texdir}/texmf-dist/metapost/bpolynomial/

%files -n texlive-bpolynomial-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/metapost/bpolynomial/

%files -n texlive-bracketkey
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bracketkey/

%files -n texlive-bracketkey-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bracketkey/

%files -n texlive-braids
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/braids/

%files -n texlive-braids-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/braids/

%files -n texlive-braille
%{_texdir}/texmf-dist/tex/latex/braille/

%files -n texlive-braille-doc
%{_texdir}/texmf-dist/doc/latex/braille/

%files -n texlive-braket
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/braket/

%files -n texlive-braket-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/braket/

%files -n texlive-brandeis-dissertation
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/brandeis-dissertation/

%files -n texlive-brandeis-dissertation-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/brandeis-dissertation/

%files -n texlive-breakurl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/breakurl/

%files -n texlive-breakurl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/breakurl/

%files -n texlive-breqn
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/breqn/

%files -n texlive-breqn-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/breqn/

%files -n texlive-br-lex
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/br-lex/

%files -n texlive-br-lex-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/br-lex/

%files -n texlive-bropd
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bropd/

%files -n texlive-bropd-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bropd/

%files -n texlive-brushscr
%license pd.txt
%{_texdir}/texmf-dist/dvips/brushscr/
%{_texdir}/texmf-dist/fonts/afm/public/brushscr/
%{_texdir}/texmf-dist/fonts/map/dvips/brushscr/
%{_texdir}/texmf-dist/fonts/tfm/public/brushscr/
%{_texdir}/texmf-dist/fonts/type1/public/brushscr/
%{_texdir}/texmf-dist/fonts/vf/public/brushscr/
%{_texdir}/texmf-dist/tex/latex/brushscr/

%files -n texlive-brushscr-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/brushscr/

%files -n texlive-bullcntr
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bullcntr/

%files -n texlive-bullcntr-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bullcntr/

%files -n texlive-burmese
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/map/dvips/burmese/
%{_texdir}/texmf-dist/fonts/tfm/public/burmese/
%{_texdir}/texmf-dist/fonts/type1/public/burmese/
%{_texdir}/texmf-dist/tex/latex/burmese/

%files -n texlive-burmese-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/burmese/

%files -n texlive-bussproofs
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/bussproofs/

%files -n texlive-bussproofs-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/bussproofs/

%files -n texlive-bxbase
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxbase/

%files -n texlive-bxbase-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxbase/

%files -n texlive-bxcjkjatype
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxcjkjatype/

%files -n texlive-bxcjkjatype-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxcjkjatype/

%files -n texlive-bxdpx-beamer
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxdpx-beamer/

%files -n texlive-bxdpx-beamer-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxdpx-beamer/

%files -n texlive-bxeepic
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxeepic/

%files -n texlive-bxeepic-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxeepic/

%files -n texlive-bxjscls
%license bsd.txt
%{_texdir}/texmf-dist/tex/latex/bxjscls/

%files -n texlive-bxjscls-doc
%license bsd.txt
%{_texdir}/texmf-dist/doc/latex/bxjscls/

%files -n texlive-bxpdfver
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxpdfver/

%files -n texlive-bxpdfver-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxpdfver/

%files -n texlive-bytefield
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/bytefield/

%files -n texlive-bytefield-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/bytefield/

%files -n texlive-c90
%{_texdir}/texmf-dist/fonts/enc/dvips/c90/

%files -n texlive-c90-doc
%{_texdir}/texmf-dist/doc/fonts/enc/c90/

%files -n texlive-cabin
%license ofl.txt
%{_datadir}/fonts/cabin
%{_texdir}/texmf-dist/fonts/enc/dvips/cabin/
%{_texdir}/texmf-dist/fonts/map/dvips/cabin/
%{_texdir}/texmf-dist/fonts/opentype/impallari/cabin/
%{_texdir}/texmf-dist/fonts/tfm/impallari/cabin/
%{_texdir}/texmf-dist/fonts/type1/impallari/cabin/
%{_texdir}/texmf-dist/fonts/vf/impallari/cabin/
%{_texdir}/texmf-dist/tex/latex/cabin/

%files -n texlive-cabin-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/cabin/

%files -n texlive-caladea
%license apache2.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/caladea/
%{_texdir}/texmf-dist/fonts/map/dvips/caladea/
%{_texdir}/texmf-dist/fonts/tfm/huerta/caladea/
%{_texdir}/texmf-dist/fonts/truetype/huerta/caladea/
%{_texdir}/texmf-dist/fonts/type1/huerta/caladea/
%{_texdir}/texmf-dist/fonts/vf/huerta/caladea/
%{_texdir}/texmf-dist/tex/latex/caladea/

%files -n texlive-caladea-doc
%license apache2.txt
%{_texdir}/texmf-dist/doc/fonts/caladea/

%files -n texlive-calcage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/calcage/

%files -n texlive-calcage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/calcage/

%files -n texlive-calctab
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/calctab/

%files -n texlive-calctab-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/calctab/

%files -n texlive-calculation
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/calculation/

%files -n texlive-calculation-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/calculation/

%files -n texlive-calculator
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/calculator/

%files -n texlive-calculator-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/calculator/

%files -n texlive-calligra
%{_texdir}/texmf-dist/fonts/source/public/calligra/
%{_texdir}/texmf-dist/fonts/tfm/public/calligra/

%files -n texlive-calligra-doc
%{_texdir}/texmf-dist/doc/latex/calligra/

%files -n texlive-calligra-type1
%{_texdir}/texmf-dist/fonts/afm/public/calligra-type1/
%{_texdir}/texmf-dist/fonts/map/dvips/calligra-type1/
%{_texdir}/texmf-dist/fonts/type1/public/calligra-type1/

%files -n texlive-calligra-type1-doc
%{_texdir}/texmf-dist/doc/fonts/calligra-type1/

%files -n texlive-calrsfs
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/calrsfs/

%files -n texlive-calrsfs-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/calrsfs/

%files -n texlive-cals
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cals/

%files -n texlive-cals-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cals/

%files -n texlive-calxxxx-yyyy
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/calxxxx-yyyy/

%files -n texlive-calxxxx-yyyy-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/calxxxx-yyyy/

%files -n texlive-cancel
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/cancel/

%files -n texlive-cancel-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/cancel/

%files -n texlive-canoniclayout
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/canoniclayout/

%files -n texlive-canoniclayout-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/canoniclayout/

%files -n texlive-cantarell
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/afm/public/cantarell/
%{_texdir}/texmf-dist/fonts/enc/dvips/cantarell/
%{_texdir}/texmf-dist/fonts/map/dvips/cantarell/
%{_texdir}/texmf-dist/fonts/tfm/public/cantarell/
%{_texdir}/texmf-dist/fonts/type1/public/cantarell/
%{_texdir}/texmf-dist/fonts/vf/public/cantarell/
%{_texdir}/texmf-dist/tex/latex/cantarell/

%files -n texlive-cantarell-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/cantarell/

%files -n texlive-captcont
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/captcont/

%files -n texlive-captcont-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/captcont/

%files -n texlive-captdef
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/captdef/

%files -n texlive-captdef-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/captdef/

%files -n texlive-caption
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/caption/

%files -n texlive-caption-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/caption/

%files -n texlive-capt-of
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/capt-of/

%files -n texlive-capt-of-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/capt-of/

%files -n texlive-carlisle
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/carlisle/

%files -n texlive-carlisle-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/carlisle/

%files -n texlive-carlito
%license ofl.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/carlito/
%{_texdir}/texmf-dist/fonts/map/dvips/carlito/
%{_texdir}/texmf-dist/fonts/tfm/typoland/carlito/
%{_texdir}/texmf-dist/fonts/truetype/typoland/carlito/
%{_texdir}/texmf-dist/fonts/type1/typoland/carlito/
%{_texdir}/texmf-dist/fonts/vf/typoland/carlito/
%{_texdir}/texmf-dist/tex/latex/carlito/

%files -n texlive-carlito-doc
%license ofl.txt
%{_texdir}/texmf-dist/doc/fonts/carlito/

%files -n texlive-carolmin-ps
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/afm/public/carolmin-ps/
%{_texdir}/texmf-dist/fonts/map/dvips/carolmin-ps/
%{_texdir}/texmf-dist/fonts/type1/public/carolmin-ps/

%files -n texlive-carolmin-ps-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/carolmin-ps/

%files -n texlive-cascadilla
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/cascadilla/
%{_texdir}/texmf-dist/tex/latex/cascadilla/

%files -n texlive-cascadilla-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cascadilla/

%files -n texlive-cases
%license pd.txt
%{_texdir}/texmf-dist/tex/latex/cases/

%files -n texlive-cases-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/cases/

%files -n texlive-casyl
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/casyl/
%{_texdir}/texmf-dist/fonts/tfm/public/casyl/
%{_texdir}/texmf-dist/tex/latex/casyl/

%files -n texlive-casyl-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/casyl/

%files -n texlive-catchfilebetweentags
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/catchfilebetweentags/

%files -n texlive-catchfilebetweentags-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/catchfilebetweentags/

%files -n texlive-catcodes
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/catcodes/

%files -n texlive-catcodes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/catcodes/

%files -n texlive-catechis
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/catechis/

%files -n texlive-catechis-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/catechis/

%files -n texlive-catoptions
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/catoptions/

%files -n texlive-catoptions-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/catoptions/

%files -n texlive-cbcoptic
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/source/public/cbcoptic/
%{_texdir}/texmf-dist/fonts/tfm/public/cbcoptic/
%{_texdir}/texmf-dist/fonts/type1/public/cbcoptic/
%{_texdir}/texmf-dist/tex/latex/cbcoptic/

%files -n texlive-cbcoptic-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cbcoptic/

%files -n texlive-cbfonts-fd
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cbfonts-fd/

%files -n texlive-cbfonts-fd-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/cbfonts-fd/

%files -n texlive-cbfonts
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/cbfonts/
%{_texdir}/texmf-dist/fonts/map/dvips/cbfonts/
%{_texdir}/texmf-dist/fonts/source/public/cbfonts/
%{_texdir}/texmf-dist/fonts/tfm/public/cbfonts/
%{_texdir}/texmf-dist/fonts/type1/public/cbfonts/

%files -n texlive-cbfonts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/fonts/cbfonts/

%files -n texlive-ccaption
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/ccaption/

%files -n texlive-ccaption-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/ccaption/

%files -n texlive-ccfonts
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/ccfonts/

%files -n texlive-ccfonts-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/ccfonts/

%files -n texlive-ccicons
%license lppl1.3.txt
%{_datadir}/fonts/ccicons
%{_texdir}/texmf-dist/fonts/enc/dvips/ccicons/
%{_texdir}/texmf-dist/fonts/map/dvips/ccicons/
%{_texdir}/texmf-dist/fonts/opentype/public/ccicons/
%{_texdir}/texmf-dist/fonts/tfm/public/ccicons/
%{_texdir}/texmf-dist/fonts/type1/public/ccicons/
%{_texdir}/texmf-dist/tex/latex/ccicons/

%files -n texlive-ccicons-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/ccicons/
%{_texdir}/texmf-dist/doc/latex/ccicons/

%files -n texlive-cclicenses
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cclicenses/

%files -n texlive-cclicenses-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cclicenses/

%files -n texlive-cc-pl
%license pd.txt
%{_texdir}/texmf-dist/fonts/map/dvips/cc-pl/
%{_texdir}/texmf-dist/fonts/source/public/cc-pl/
%{_texdir}/texmf-dist/fonts/tfm/public/cc-pl/
%{_texdir}/texmf-dist/fonts/type1/public/cc-pl/

%files -n texlive-cc-pl-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/cc-pl/

%files -n texlive-cd-cover
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/cd-cover/

%files -n texlive-cd-cover-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cd-cover/

%files -n texlive-cdpbundl
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cdpbundl/

%files -n texlive-cdpbundl-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cdpbundl/

%files -n texlive-cd
%license gpl.txt
%{_texdir}/texmf-dist/tex/latex/cd/

%files -n texlive-cd-doc
%license gpl.txt
%{_texdir}/texmf-dist/doc/latex/cd/

%files -n texlive-cellspace
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/cellspace/

%files -n texlive-cellspace-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/cellspace/

%files -n texlive-cell
%license pd.txt
%{_texdir}/texmf-dist/bibtex/bst/cell/
%{_texdir}/texmf-dist/tex/latex/cell/

%files -n texlive-cell-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/latex/cell/

%files -n texlive-celtic
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/celtic/

%files -n texlive-celtic-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/celtic/

%files -n texlive-censor
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/censor/

%files -n texlive-censor-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/censor/

%files -n texlive-cfr-initials
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/cfr-initials/

%files -n texlive-cfr-initials-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/cfr-initials/

%files -n texlive-cfr-lm
%license lppl1.3.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/cfr-lm/
%{_texdir}/texmf-dist/fonts/map/dvips/cfr-lm/
%{_texdir}/texmf-dist/fonts/tfm/public/cfr-lm/
%{_texdir}/texmf-dist/fonts/vf/public/cfr-lm/
%{_texdir}/texmf-dist/tex/latex/cfr-lm/

%files -n texlive-cfr-lm-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/cfr-lm/

%files -n texlive-changebar
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/changebar/

%files -n texlive-changebar-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/changebar/

%files -n texlive-changelayout
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/changelayout/

%files -n texlive-changelayout-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/changelayout/

%files -n texlive-changepage
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/changepage/

%files -n texlive-changepage-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/changepage/

%files -n texlive-changes
%license lppl1.3.txt
%{_texdir}/texmf-dist/scripts/changes/
%{_texdir}/texmf-dist/tex/latex/changes/

%files -n texlive-changes-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/changes/

%files -n texlive-chappg
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chappg/

%files -n texlive-chappg-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chappg/

%files -n texlive-chapterfolder
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chapterfolder/

%files -n texlive-chapterfolder-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chapterfolder/

%files -n texlive-charter
%{_texdir}/texmf-dist/fonts/afm/bitstrea/charter/
%{_texdir}/texmf-dist/fonts/tfm/bitstrea/charter/
%{_texdir}/texmf-dist/fonts/type1/bitstrea/charter/
%{_texdir}/texmf-dist/fonts/vf/bitstrea/charter/

%files -n texlive-charter-doc
%{_texdir}/texmf-dist/doc/fonts/charter/

%files -n texlive-chbibref
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chbibref/

%files -n texlive-chbibref-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chbibref/

%files -n texlive-chemarrow
%license pd.txt
%{_texdir}/texmf-dist/fonts/afm/public/chemarrow/
%{_texdir}/texmf-dist/fonts/map/dvips/chemarrow/
%{_texdir}/texmf-dist/fonts/source/public/chemarrow/
%{_texdir}/texmf-dist/fonts/tfm/public/chemarrow/
%{_texdir}/texmf-dist/fonts/type1/public/chemarrow/
%{_texdir}/texmf-dist/tex/latex/chemarrow/

%files -n texlive-chemarrow-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/chemarrow/

%files -n texlive-chembst
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/chembst/

%files -n texlive-chembst-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chembst/

%files -n texlive-chemcompounds
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chemcompounds/

%files -n texlive-chemcompounds-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chemcompounds/

%files -n texlive-chemcono
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chemcono/

%files -n texlive-chemcono-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chemcono/

%files -n texlive-chemexec
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chemexec/

%files -n texlive-chemexec-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chemexec/

%files -n texlive-chemfig
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/chemfig/

%files -n texlive-chemfig-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/chemfig/

%files -n texlive-chemformula
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chemformula/

%files -n texlive-chemformula-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chemformula/

%files -n texlive-chemgreek
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chemgreek/

%files -n texlive-chemgreek-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chemgreek/

%files -n texlive-chem-journal
%license gpl.txt
%{_texdir}/texmf-dist/bibtex/bst/chem-journal/

%files -n texlive-chemmacros
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chemmacros/

%files -n texlive-chemmacros-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chemmacros/

%files -n texlive-chemnum
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chemnum/

%files -n texlive-chemnum-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chemnum/

%files -n texlive-chemschemex
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/chemschemex/

%files -n texlive-chemschemex-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/chemschemex/

%files -n texlive-chemstyle
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chemstyle/

%files -n texlive-chemstyle-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chemstyle/

%files -n texlive-cherokee
%{_texdir}/texmf-dist/fonts/source/public/cherokee/
%{_texdir}/texmf-dist/fonts/tfm/public/cherokee/
%{_texdir}/texmf-dist/tex/latex/cherokee/

%files -n texlive-cherokee-doc
%{_texdir}/texmf-dist/doc/fonts/cherokee/

%files -n texlive-chessboard
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chessboard/

%files -n texlive-chessboard-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chessboard/

%files -n texlive-chessfss
%license lppl1.txt
%{_texdir}/texmf-dist/fonts/enc/dvips/chessfss/
%{_texdir}/texmf-dist/tex/latex/chessfss/

%files -n texlive-chessfss-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chessfss/

%files -n texlive-chess-problem-diagrams
%license lppl1.2.txt
%{_texdir}/texmf-dist/tex/latex/chess-problem-diagrams/

%files -n texlive-chess-problem-diagrams-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/chess-problem-diagrams/

%files -n texlive-chess
%license pd.txt
%{_texdir}/texmf-dist/fonts/source/public/chess/
%{_texdir}/texmf-dist/fonts/tfm/public/chess/
%{_texdir}/texmf-dist/tex/latex/chess/

%files -n texlive-chess-doc
%license pd.txt
%{_texdir}/texmf-dist/doc/fonts/chess/

%files -n texlive-chet
%license lppl1.3.txt
%{_texdir}/texmf-dist/bibtex/bst/chet/
%{_texdir}/texmf-dist/tex/latex/chet/

%files -n texlive-chet-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chet/

%files -n texlive-chextras
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chextras/

%files -n texlive-chextras-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chextras/

%files -n texlive-chicago-annote
%license lppl1.txt
%{_texdir}/texmf-dist/bibtex/bst/chicago-annote/

%files -n texlive-chicago-annote-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/bibtex/chicago-annote/

%files -n texlive-chicago
%{_texdir}/texmf-dist/bibtex/bst/chicago/
%{_texdir}/texmf-dist/tex/latex/chicago/

%files -n texlive-chickenize
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/luatex/chickenize/

%files -n texlive-chickenize-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/luatex/chickenize/

%files -n texlive-chkfloat
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chkfloat/

%files -n texlive-chkfloat-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chkfloat/

%files -n texlive-chletter
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chletter/

%files -n texlive-chletter-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chletter/

%files -n texlive-chngcntr
%license lppl1.txt
%{_texdir}/texmf-dist/tex/latex/chngcntr/

%files -n texlive-chngcntr-doc
%license lppl1.txt
%{_texdir}/texmf-dist/doc/latex/chngcntr/

%files -n texlive-chronology
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chronology/

%files -n texlive-chronology-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/chronology/

%files -n texlive-chronosys
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/generic/chronosys/

%files -n texlive-chronosys-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/generic/chronosys/

%files -n texlive-chscite
%license lppl1.2.txt
%{_texdir}/texmf-dist/bibtex/bst/chscite/
%{_texdir}/texmf-dist/tex/latex/chscite/

%files -n texlive-chscite-doc
%license lppl1.2.txt
%{_texdir}/texmf-dist/doc/latex/chscite/

%files -n texlive-breakcites-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/breakcites/

%files -n texlive-breakcites
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/breakcites/

%files -n texlive-bxdvidriver-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxdvidriver/

%files -n texlive-bxdvidriver
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxdvidriver/

%files -n texlive-bxenclose-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxenclose/

%files -n texlive-bxenclose
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxenclose/

%files -n texlive-bxnewfont-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxnewfont/

%files -n texlive-bxnewfont
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxnewfont/

%files -n texlive-bxpapersize-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/bxpapersize/

%files -n texlive-bxpapersize
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/bxpapersize/

%files -n texlive-carbohydrates-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/latex/carbohydrates/

%files -n texlive-carbohydrates
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/carbohydrates/

%files -n texlive-chivo-doc
%license lppl1.3.txt
%{_texdir}/texmf-dist/doc/fonts/chivo/

%files -n texlive-chivo
%license lppl1.3.txt
%{_texdir}/texmf-dist/tex/latex/chivo/
%{_texdir}/texmf-dist/fonts/opentype/public/chivo/
%{_texdir}/texmf-dist/fonts/map/dvips/chivo/
%{_texdir}/texmf-dist/fonts/tfm/public/chivo/
%{_texdir}/texmf-dist/fonts/vf/public/chivo/
%{_texdir}/texmf-dist/fonts/enc/dvips/chivo/
%{_texdir}/texmf-dist/fonts/type1/public/chivo/

%files -n texlive-churchslavonic-doc
%license other-free.txt
%{_texdir}/texmf-dist/doc/latex/churchslavonic/

%files -n texlive-churchslavonic
%license other-free.txt
%{_texdir}/texmf-dist/tex/latex/churchslavonic/


%files -n texlive-bredzenie
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/bredzenie/
%{_texdir}/texmf-dist/tex/latex/bredzenie/

%files -n texlive-bxcalc
%doc %{_texdir}/texmf-dist/doc/latex/bxcalc/
%{_texdir}/texmf-dist/tex/latex/bxcalc/

%files -n texlive-bxjalipsum
%doc %{_texdir}/texmf-dist/doc/latex/bxjalipsum/
%{_texdir}/texmf-dist/tex/latex/bxjalipsum/

%files -n texlive-bxjaprnind
%doc %{_texdir}/texmf-dist/doc/latex/bxjaprnind/
%{_texdir}/texmf-dist/tex/latex/bxjaprnind/

%files -n texlive-bxorigcapt
%doc %{_texdir}/texmf-dist/doc/latex/bxorigcapt/
%{_texdir}/texmf-dist/tex/latex/bxorigcapt/

%files -n texlive-callouts
%license lppl.txt
%doc %{_texdir}/texmf-dist/doc/latex/callouts/
%{_texdir}/texmf-dist/tex/latex/callouts/

%files -n texlive-cesenaexam
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/cesenaexam/
%{_texdir}/texmf-dist/tex/latex/cesenaexam/

%files -n texlive-cheatsheet
%doc %{_texdir}/texmf-dist/doc/latex/cheatsheet/
%{_texdir}/texmf-dist/tex/latex/cheatsheet/

%files -n texlive-childdoc
%license lppl1.3.txt
%doc %{_texdir}/texmf-dist/doc/latex/childdoc/
%{_texdir}/texmf-dist/tex/latex/childdoc/

%files -n texlive-cascade
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/cascade/
%doc %{_texdir}/texmf-dist/doc/latex/cascade/

%files -n texlive-cellprops
%license gpl3.txt
%{_texdir}/texmf-dist/tex/latex/cellprops/
%doc %{_texdir}/texmf-dist/doc/latex/cellprops/

%files -n texlive-chemsec
%license lppl.txt
%{_texdir}/texmf-dist/tex/latex/chemsec/
%doc %{_texdir}/texmf-dist/doc/latex/chemsec/


%changelog
* Wed May 19 2021 maminjie <maminjie1@huawei.com> - 8:2018-24
- split texlive

* Fri Sep 11 2020 Guoshuai Sun <sunguoshuai@huawei.com> - 8:2018-23
- Drop texlive-texinfo,use new files in texinfo-tex instead

* Sun Jan 19 2020 daiqianwen <daiqianwen@huawei.com> - 8:2018-22
- Type:bugfix
- ID:NA
- SUG:NA
- DESC: modify spec

* Tue Dec 10 2019 Jiangping Hu <hujiangping@huawei.com> - 8:2018-21
- Package init
