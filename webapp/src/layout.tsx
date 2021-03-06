import React from "react";
import NextLink from "next/link";
import { useRouter } from "next/router";
import {
  AppBar,
  Button,
  Container,
  Link as MaterialLink,
  makeStyles,
  Toolbar,
  Typography,
} from "@material-ui/core";
import { ArrowBack } from "@material-ui/icons";

const useStyles = makeStyles((theme) => ({
  navContainer: {
    marginTop: theme.spacing(4),
  },
  mainContainer: {
    marginTop: theme.spacing(4),
    marginBottom: theme.spacing(4),
  },
}));

export const Layout: React.FunctionComponent = (props) => {
  const router = useRouter();
  const styles = useStyles();

  return (
    <>
      <AppBar position="relative">
        <Toolbar>
          <Typography variant="h6" component="span" noWrap>
            <NextLink href="/" passHref>
              <MaterialLink color="inherit" underline="none">
                saltcandy123font
              </MaterialLink>
            </NextLink>
          </Typography>
        </Toolbar>
      </AppBar>
      {router.pathname !== "/" && (
        <Container component="nav" className={styles.navContainer}>
          <Typography variant="body1">
            <NextLink href="/" passHref>
              <Button>
                <ArrowBack />
                Back to home
              </Button>
            </NextLink>
          </Typography>
        </Container>
      )}
      <Container component="main" className={styles.mainContainer}>
        <>{props.children}</>
      </Container>
    </>
  );
};
