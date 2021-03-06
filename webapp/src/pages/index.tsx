import React from "react";
import { NextPage } from "next";
import NextLink from "next/link";
import {
  Button,
  Container,
  Grid,
  makeStyles,
  Typography,
} from "@material-ui/core";
import { Layout } from "@src/layout";

const useStyles = makeStyles({
  pageTitle: {
    wordBreak: "break-word",
  },
});

const Homepage: NextPage = () => {
  const styles = useStyles();

  return (
    <Layout>
      <Container maxWidth="sm">
        <Typography
          className={styles.pageTitle}
          variant="h3"
          component="h1"
          gutterBottom
        >
          saltcandy123font
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
        <Grid container spacing={2} justify="center">
          <Grid item>
            <Button
              color="primary"
              variant="contained"
              href="https://github.com/saltcandy123/saltcandy123font/releases"
            >
              Download
            </Button>
          </Grid>
          <Grid item>
            <NextLink href="/demo" passHref>
              <Button color="default" variant="contained">
                Demo
              </Button>
            </NextLink>
          </Grid>
          <Grid item>
            <NextLink href="/glyphs" passHref>
              <Button color="default" variant="contained">
                All glyphs
              </Button>
            </NextLink>
          </Grid>
        </Grid>
      </Container>
    </Layout>
  );
};

export default Homepage;
