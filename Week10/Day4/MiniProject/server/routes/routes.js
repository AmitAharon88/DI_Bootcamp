import express from "express";
import { _registerUser, _checkForUser } from "../controllers/users.js";

const router = express.Router();

router.post("/register", _registerUser);
router.post("/login", _checkForUser);

export default router;