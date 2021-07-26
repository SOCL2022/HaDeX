import { AskRequest, AskResponse, ChatRequest } from "./models";

export async function askApi(options: AskRequest): Promise<AskResponse> {
    const response