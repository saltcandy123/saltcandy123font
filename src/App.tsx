import React from "react";
import {
  AppBar,
  Box,
  Container,
  CssBaseline,
  TextField,
  ThemeProvider,
  Toolbar,
  Typography,
  createTheme,
  Button,
  IconButton,
  Link,
} from "@mui/material";
import { GitHub } from "@mui/icons-material";

const theme = createTheme({
  typography: {
    fontSize: 16,
    fontFamily: '"saltcandy123font"',
  },
});

export function App(): JSX.Element {
  const [text, setText] = React.useState<string>("");
  const onChange = React.useCallback<
    React.ChangeEventHandler<HTMLInputElement | HTMLTextAreaElement>
  >((e) => {
    setText(e.target.value);
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <AppBar position="relative">
        <Toolbar sx={{ width: "100%", maxWidth: "md", ml: "auto", mr: "auto" }}>
          <Typography component="h1" noWrap sx={{ flexGrow: 1 }} variant="h6">
            <Link color="inherit" href="." underline="none">
              saltcandy123font
            </Link>
          </Typography>
          <Button
            color="inherit"
            href="https://github.com/saltcandy123/saltcandy123font/releases/latest"
          >
            Download
          </Button>
          <IconButton
            aria-label="GitHub repository"
            color="inherit"
            href="https://github.com/saltcandy123/saltcandy123font"
          >
            <GitHub />
          </IconButton>
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
        <Box mb={4}>
          <TextField
            InputLabelProps={{ sx: { fontFamily: "sans-serif" } }}
            InputProps={{ sx: { fontFamily: "sans-serif" } }}
            fullWidth
            label="Type something here"
            multiline
            onChange={onChange}
            variant="filled"
          />
        </Box>
        <Typography
          component="p"
          gutterBottom
          sx={{
            wordBreak: "break-word",
          }}
        >
          {text
            .split("\n")
            // eslint-disable-next-line react/no-array-index-key
            .map((line, idx) => [idx > 0 && <br key={idx} />, line])}
        </Typography>
      </Container>
    </ThemeProvider>
  );
}
