import React from "react";
import { NextPage } from "next";
import NextLink from "next/link";
import {
  Box,
  TextField,
  AppBar,
  Container,
  Link as MaterialLink,
  makeStyles,
  Toolbar,
  Typography,
} from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  mainContainer: {
    marginTop: theme.spacing(4),
    marginBottom: theme.spacing(4),
  },
  pageTitle: {
    wordBreak: "break-word",
  },
  textField: {
    fontFamily: "sans-serif",
  },
  textPreview: {
    wordBreak: "break-word",
  },
}));

const Homepage: NextPage = () => {
  const styles = useStyles();
  const [text, setText] = React.useState<string>("");

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
      <Container
        component="main"
        maxWidth="md"
        className={styles.mainContainer}
      >
        <Typography
          className={styles.pageTitle}
          variant="h3"
          component="h1"
          gutterBottom
        >
          saltcandy123font
        </Typography>
        <Typography variant="body1" paragraph>
          This is a handwritten font created by @saltcandy123. That&apos;s it!
        </Typography>
        <Typography variant="h4" component="h2" gutterBottom>
          Download
        </Typography>
        <Typography variant="body1" paragraph>
          <a href="https://github.com/saltcandy123/saltcandy123font/releases/latest">
            Download the latest version of the font here.
          </a>
        </Typography>
        <Typography
          className={styles.pageTitle}
          variant="h4"
          component="h2"
          gutterBottom
        >
          Demos
        </Typography>
        <Typography variant="body1" paragraph>
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat. Duis aute irure dolor in
          reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
          pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
          culpa qui officia deserunt mollit anim id est laborum.
        </Typography>
        <Box mb={4}>
          <TextField
            multiline
            fullWidth
            variant="filled"
            label="Type something here"
            InputLabelProps={{ className: styles.textField }}
            InputProps={{ className: styles.textField }}
            onChange={(e) => setText(e.target.value)}
          />
        </Box>
        <Typography component="p" className={styles.textPreview}>
          {text
            .split("\n")
            .map((line, idx) => [idx > 0 && <br key={idx} />, line])}
        </Typography>
      </Container>
    </>
  );
};

export default Homepage;
