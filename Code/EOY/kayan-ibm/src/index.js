import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.scss';
import App from './App';
import reportWebVitals from './reportWebVitals';
import {
  HeaderContainer,
  Header,
  SkipToContent,
  HeaderMenuButton,
  HeaderName,
  HeaderNavigation,
  HeaderMenuItem,
  HeaderMenu,
  HeaderGlobalBar,
  HeaderGlobalAction,
  Search,
  SideNav,
  SideNavItems,
  SideNavMenu,
  SideNavMenuItem,
  Theme,
  SideNavLink
} from '@carbon/react';
import { 
  Bee, 
  Badge, 
  ChartColumn
} from "@carbon/icons-react";

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    { /*
    <Header aria-label="IBM Platform Name">
       <HeaderName href="#" prefix="IBM">
         [Platform]
       </HeaderName>
     </Header>
     */ } 
     <Theme theme="g100">
      <HeaderContainer
        render={({ isSideNavExpanded, onClickSideNavExpand }) => (
          <>
            <Header aria-label="Header">
              <SkipToContent />
              <HeaderMenuButton
                aria-label={isSideNavExpanded ? 'Close menu' : 'Open menu'}
                isCollapsible
                onClick={onClickSideNavExpand}
                isActive={isSideNavExpanded}
              />
              <HeaderName href="#" prefix="Kayan Intwala">
                12 Month Review
              </HeaderName>
              <HeaderNavigation aria-label="Kayan 12 Month">
              </HeaderNavigation>
              <HeaderGlobalBar>
                {/* <HeaderGlobalAction
                  aria-label="Search"
                  onClick={console.log('test')}>
                  <Search size={20} />
                </HeaderGlobalAction> */}
                {/* <HeaderGlobalAction
                  aria-label="Notifications"
                  onClick={console.log('test')}>
                  <Notification size={20} /> 
                </HeaderGlobalAction> */}
                {/* <HeaderGlobalAction
                  aria-label="App Switcher"
                  // onClick={action('app-switcher click')}
                  tooltipAlignment="end">
                  {/* <SwitcherIcon size={20} />
                </HeaderGlobalAction> */}
              </HeaderGlobalBar>
              <SideNav
                aria-label="Side navigation"
                isRail
                expanded={isSideNavExpanded}
                onOverlayClick={onClickSideNavExpand}>
                <SideNavItems>
                  <SideNavLink renderIcon={Bee} href='' large>
                    Top
                  </SideNavLink>
                  <SideNavLink renderIcon={Badge} href='' large>
                    Badges
                  </SideNavLink>
                  <SideNavLink renderIcon={ChartColumn} href='' large>
                    Stats
                  </SideNavLink>
                </SideNavItems>
              </SideNav>
            </Header>
          </>
        )}
      />
      </Theme>
    <App/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();

