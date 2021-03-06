import React, { useEffect } from "react";
import { NextPage } from "next";
import { useRouter } from "next/router";
import { Container, Typography } from "@material-ui/core";
import { Layout } from "@src/layout";

const NotFoundPage: NextPage = () => {
  const router = useRouter();

  useEffect(() => {
    router.push("/");
  });

  return (
    <Layout>
      <Container maxWidth="sm">
        <Typography variant="h3" component="h1" gutterBottom>
          Not found
        </Typography>
      </Container>
    </Layout>
  );
};

export default NotFoundPage;
