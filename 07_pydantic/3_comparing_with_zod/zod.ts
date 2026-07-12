import * as z from 'zod';

export const ZodUserSchema = z.object({
    username: z.string()
            .trim()
            .toLowerCase()
            .min(3, "Username must be at least 3 characters")
            .max(10, "Username must be at most 10 characters")
            .regex(
                /^[a-z0-9]+$/,
                "Username can only contain lowercase letters (a-z) and numbers (0-9)"
            ),

    firstName: z.string()
            .max(15, "First name must at be at most 15 chars")
            .regex(
                /^[a-zA-Z]+$/,
                "First Name can only contain letters"
            )
            .trim(),

    lastName: z.string()
            .max(15, "Last name must at be at most 15 chars")
            .regex(
                /^[a-zA-Z]+$/,
                "Last Name can only contain letters"
            )
            .trim(),

    password: z.string()
            .min(6, "Password must be at least 6 characters")
            .regex(/\d/, "Password must contain at least one number")
            .regex(/[^\w\s]/, "Password must contain at least one special character")
});