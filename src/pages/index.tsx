import React from "react";
import { NextPage } from "next";
import NextLink from "next/link";
import {
  Box,
  TextField,
  AppBar,
  Container,
  Link as MaterialLink,
  Toolbar,
  Typography,
} from "@mui/material";

const Homepage: NextPage = () => {
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
        sx={{
          mt: 4,
          mb: 4,
        }}
      >
        <Typography
          sx={{
            wordBreak: "break-word",
          }}
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
        <Typography variant="h4" component="h2" gutterBottom>
          Sample text
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
        <Typography variant="h4" component="h2" gutterBottom>
          Try with your text
        </Typography>
        <Box mb={4}>
          <TextField
            multiline
            fullWidth
            variant="filled"
            label="Type something here"
            InputLabelProps={{ sx: { fontFamily: "sans-serif" } }}
            InputProps={{ sx: { fontFamily: "sans-serif" } }}
            onChange={(e) => setText(e.target.value)}
          />
        </Box>
        <Typography
          component="p"
          sx={{
            wordBreak: "break-word",
          }}
          gutterBottom
        >
          {text
            .split("\n")
            .map((line, idx) => [idx > 0 && <br key={idx} />, line])}
        </Typography>
      </Container>
    </>
  );
};

export default Homepage;
