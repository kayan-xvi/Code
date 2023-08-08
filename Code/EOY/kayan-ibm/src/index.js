import React from "react";
import ReactDOM from "react-dom/client";
import "./index.scss";
import App from "./App";
import {
  HeaderContainer,
  Header,
  SkipToContent,
  HeaderMenuButton,
  HeaderName,
  HeaderNavigation,
  HeaderGlobalBar,
  SideNav,
  SideNavItems,
  Theme,
  SideNavLink,
} from "@carbon/react";
import { Popup ,Badge, ChartColumn, Events, Camera, ViewNext} from "@carbon/icons-react";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(
  <React.StrictMode>
    <Theme theme="g100">
      <HeaderContainer
        render={({ isSideNavExpanded, onClickSideNavExpand }) => (
          <>
            <Header aria-label="Header">
              <SkipToContent />
              <HeaderMenuButton
                aria-label={isSideNavExpanded ? "Close menu" : "Open menu"}
                isCollapsible
                onClick={onClickSideNavExpand}
                isActive={isSideNavExpanded}
              />
              <HeaderName href="#" prefix="Kayan Intwala">
                12 Month Review
              </HeaderName>
              <HeaderNavigation aria-label="Kayan 12 Month"></HeaderNavigation>
              <HeaderGlobalBar>
              </HeaderGlobalBar>
              <SideNav
                aria-label="Side navigation"
                isRail
                expanded={isSideNavExpanded}
                onOverlayClick={onClickSideNavExpand}
                className="scroll"
              >
                <SideNavItems>
                <SideNavLink renderIcon={Popup} href="#presentation" large>
                    Presentation
                  </SideNavLink>
                  <SideNavLink renderIcon={Camera} href="#gallery" large>
                    Gallery
                  </SideNavLink>
                  <SideNavLink renderIcon={Events} href="#roles" large>
                    Roles
                  </SideNavLink>
                  <SideNavLink renderIcon={ChartColumn} href="#stats" large>
                    Stats
                  </SideNavLink>
                  <SideNavLink renderIcon={Badge} href="#badges" large>
                    Badges
                  </SideNavLink>
                  <SideNavLink renderIcon={ViewNext} href="#next-steps" large>
                    What's Next? 
                  </SideNavLink>
                </SideNavItems>
              </SideNav>
            </Header>
          </>
        )}
      />
    </Theme>
    <App />
  </React.StrictMode>,
);