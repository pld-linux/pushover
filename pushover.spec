Summary:	Pushover is a fun puzzle game
Summary(hu.UTF-8):	Pushover egy vicces kirakós játék
Name:		pushover
Version:	0.0.3
Release:	1
License:	GPL v3
Group:		X11/Applications/Games
Source0:	http://dl.sourceforge.net/pushover/%{name}-%{version}.tar.gz
# Source0-md5:	831feec2d46583db01647a73295d4108
Source1:	%{name}.desktop
URL:		http://pushover.sourceforge.net/
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	lua51-devel
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Pushover is a fun puzzle game originally published by Ocean in 1992.
In this game you control an ant that can walk along platforms that are
connected with ladders. On those platforms are dominos that need to
fall according to some rules.

- All dominos must fall and none must crash into another
- One special domino must fall as last domino and that domino triggers
  the exit door to open when you enter the exit door the level has been
  completed
- You may rearrange as many dominos as you want, except for the
  trigger. You may not place dominos in front of the doors, except for
  the vanishing domino.
- You may push once to start a chain reaction with the dominos leading
  to the fall of all of them
- All this has to be done within a time limit (which is normally
  generous)
- There are 10 different dominos that behave differently when pushed,
  some fall, some not, some wait a bit before they fall, some raise,
  some toppler until they meet an obstacle
- There is a help in the game and introductory levels that show how
  all the dominos work


%description -l hu.UTF-8
Pushover egy vicces kirakós játék, amelyet eredetileg az Ocean adott
ki 1992-ben. Ebben a játékban egy hangyát irányítasz, amely szintek
között sétál, amelyek létrákkal kapcsolódnak. A szinteken dominók
vannak, amelyeket el kell dönteni megadott szabályok alapján.

- Az összes dominót érinteni kell, és egyik se törhet szét
- Egy különleges dominónak ('trigger') utolsóként el kell eldőlnie, és
  ez a dominó nyitja a kijárati ajtót, amin ha kimégy, teljesíted a
  szintet
- A dominókat tetszőlegesen átrendezheted, kivéve az ajtónyitót. Nem
  rakhatsz dominókat a kijárati ajtó elé, kivéve eltűnő dominókat
- Csak egyszer indíthatod el a láncreakciót egy kezdő dominó
  eldöntésével
- Ezeket egy megadott időn belül kell teljesítened (amely normál
  esetben bőven elég)
- 10 különböző dominó van, amelyek mind máshogy viselkednek, ha
  meglökik. Egyikük eldől, másikuk nem, némelyik vár egy kicsit, mielőtt
  elbillen, némelyik megemelkedik, némelyik addig dől, amíg akadályba
  nem ütközik
- Egy súgó van a játékban, és egy bevezető pálya is, amely megmutatja,
  hogyan működnek a dominók

%prep
%setup -q

%build
%{__sed} -i "s@lua5.1@lua51@g" configure.ac
%{__aclocal}
%{__libtoolize}
%{__autoconf}
%{__automake}
%configure \
	--disable-static
%{__make}


%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
%{__rm} -rf $RPM_BUILD_ROOT%{_docdir}/pushover/readme.txt
install -d $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%{find_lang} %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS readme.txt
%attr(755,root,root) %{_bindir}/pushover
%dir %{_datadir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
