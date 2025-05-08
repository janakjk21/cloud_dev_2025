import React, { useState } from "react";
import { Container, Row, Col, Form, Button, Alert } from "react-bootstrap";

const Login = () => {
    const [email, setEmail] = useState(""); // ✅ use email instead of username
    const [password, setPassword] = useState("");
    const [error, setError] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!email || !password) {
            setError("Please fill in all fields");
            return;
        }
        setError("");

        try {
            const response = await fetch("http://127.0.0.1:8000/auth/login", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({ email, password }), // ✅ send email instead of username
            });

            const data = await response.json();

            if (!response.ok) {
                throw new Error(data.detail || "Login failed");
            }

            console.log("Login successful:", data);

            // Save token
            sessionStorage.setItem("access_token", data.access_token);
            sessionStorage.setItem("user", JSON.stringify(data.user));

            alert("Login successful!");

        } catch (err) {
            console.error(err);
            setError(err.message);
        }
    };

    return (
        <Container className="mt-5">
            <Row className="justify-content-md-center">
                <Col md={6}>
                    <h2 className="text-center">Login</h2>
                    {error && <Alert variant="danger">{error}</Alert>}
                    <Form onSubmit={handleSubmit}>
                        <Form.Group controlId="formEmail" className="mb-3">
                            <Form.Label>Email address</Form.Label>
                            <Form.Control
                                type="email"
                                placeholder="Enter email"
                                value={email}
                                onChange={(e) => setEmail(e.target.value)}
                            />
                        </Form.Group>

                        <Form.Group controlId="formPassword" className="mb-3">
                            <Form.Label>Password</Form.Label>
                            <Form.Control
                                type="password"
                                placeholder="Enter password"
                                value={password}
                                onChange={(e) => setPassword(e.target.value)}
                            />
                        </Form.Group>

                        <Button variant="primary" type="submit" className="w-100">
                            Login
                        </Button>
                    </Form>
                </Col>
            </Row>
        </Container>
    );
};

export default Login;
